import os
from typing import Any, Union
from io import BytesIO

import django_rq

import requests

from django.conf import settings
from django.template.loader import render_to_string

from core.apps.checks.constants import CheckTypeChoices
from core.apps.checks.models import Check
from core.apps.printers.models import Printer


def create_checks(json_data: dict[str, Any]) -> list[Check]:
    point_id = json_data.pop('point_id')

    try:
        printer_kitchen_id = Printer.objects.get_kitchen_printer(
            point_id=point_id,
        ).id
    except AttributeError as e:
        # TODO: логировать
        return
    
    try:
        printer_client_id = Printer.objects.get_client_printer(
            point_id=point_id,
        ).id
    except AttributeError as e:
        # TODO: логировать
        return

    checks = Check.objects.create_both_checks(
        printer_kitchen_id=printer_kitchen_id,
        printer_client_id=printer_client_id,
        order=json_data,
    )

    for check in checks:
        # django_rq.enqueue(make_pdf, check=check)
        django_rq.enqueue(make_pdf, check=check)
    return checks


def get_pdf_path(
    order_id: int,
    check_type: str,
) -> str:
    '''
    Получить путь к пдф файлу чека для сохранения
    '''
    pdf_root = settings.PDF_PATH_ROOT
    pdf_filename = f'{order_id}_{check_type}.pdf'
    return os.path.join(pdf_root, pdf_filename)


def render_check_template(check: Check) -> str:
    '''
    Отрендерить шаблон чека в html
    '''
    context = { 'check': check }
    if check.type == CheckTypeChoices.CLIENT:
        return render_to_string('client_check.html', context=context)
    elif check.type == CheckTypeChoices.KITCHEN:
        return render_to_string('kitchen_check.html', context=context)
    return ''


def make_pdf(check: Check) -> Union[str, None]:
    '''
    Создать пдф файл для переданного чека.
    '''
    pdf_path = get_pdf_path(order_id=check.order['id'], check_type=check.type)
    template = render_check_template(check)
    
    if not template:
        return

    template_bytes = BytesIO(template.encode())
    template_bytes.seek(0)
    
    files = { 'file': template_bytes.getvalue() }
    response = requests.post(
        settings.WKHTMLTOPDF_URL,
        files=files,
    )
    
    if not response.ok:
        return

    with open(pdf_path, 'wb') as write_file:
        write_file.write(response.content)
    return pdf_path