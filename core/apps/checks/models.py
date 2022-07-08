from django.db import models

from core.apps.checks.constants import CheckStatus, CheckTypeChoices
from core.apps.checks.managers import CheckManager


class Check(models.Model):
    printer = models.ForeignKey(
        'printers.Printer',
        verbose_name='принтер',
        on_delete=models.PROTECT,
    )
    type = models.CharField(
        verbose_name='тип чека которые печатает принтер',
        choices=CheckTypeChoices.choices,
        max_length=30,
    )
    order = models.JSONField(verbose_name='информация о заказе')
    status = models.CharField(
        verbose_name='статус чека',
        max_length=20,
        choices=CheckStatus.choices,
    )
    pdf_file = models.FileField(
        verbose_name='ссылка на созданный PDF-файл',
        null=True,
        blank=True,
    )

    objects: CheckManager = CheckManager()

    class Meta:
        verbose_name = 'Чек'
        verbose_name_plural = 'Чеки'
