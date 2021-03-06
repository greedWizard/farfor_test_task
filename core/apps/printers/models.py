import uuid
from django.db import models

from core.apps.checks.constants import CheckTypeChoices
from core.apps.printers.managers import PrinterManager


class Printer(models.Model):
    name = models.CharField(
        verbose_name='название принтера',
        max_length=100,
    )
    api_key = models.UUIDField(
        verbose_name='ключ доступа к API',
        unique=True,
        default=uuid.uuid4,
    )
    check_type = models.CharField(
        verbose_name='тип чека которые печатает принтер',
        choices=CheckTypeChoices.choices,
        max_length=20,
    )
    point_id = models.IntegerField(verbose_name='точка к которой привязан принтер')

    objects: PrinterManager = PrinterManager()

    def __str__(self) -> str:
        return f'{self.name} {self.check_type}'

    def __repr__(self) -> str:
        return f'<{self.name} {self.check_type}>'

    class Meta:
        verbose_name = 'Принтер'
        verbose_name_plural = 'Принтеры'
        # constraints
        unique_together = (
            ('point_id', 'check_type'),
        )
