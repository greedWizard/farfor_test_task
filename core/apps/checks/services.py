from typing import Any

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

    created_checks = Check.objects.create_both_checks(
        printer_kitchen_id=printer_kitchen_id,
        printer_client_id=printer_client_id,
        order=json_data,
    )
    return True

