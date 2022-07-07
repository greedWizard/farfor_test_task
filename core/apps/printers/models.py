import uuid
from django.db import models

from core.apps.checks.constants import CheckTypeChoices


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
