from typing import Any
from django.db.models import Manager, Model, QuerySet, Q

from core.apps.checks.constants import CheckStatus, CheckTypeChoices


class CheckQuerySet(QuerySet):
    def avaliable_for_printing(self):
        return self.filter(
            Q(status=CheckStatus.RENDERED) | Q(status=CheckStatus.PRINTED),
            pdf_file__isnull=False,
        )


class CheckManager(Manager):
    def get_queryset(self) -> CheckQuerySet:
        return CheckQuerySet(self.model, using=self._db)

    def avaliable_for_printing(self):
        return self.get_queryset().avaliable_for_printing()

    def attach_pdf_file(self, check_id: int, filepath: str):
        '''
        Прикрепить файл с отрендеренным чеком в формате pdf
        '''
        self.filter(id=check_id).update(status=CheckStatus.RENDERED, pdf_file=filepath)

    def create_both_checks(
        self,
        order: dict[str, Any],
        printer_kitchen_id: int,
        printer_client_id: int,
    ) -> list[Model]:
        '''
        Метод создания чеков сразу для обоих принтеров по их id.
        '''
        created_objs = []

        created_objs.append(
            self.create(
                order=order,
                printer_id=printer_kitchen_id,
                type=CheckTypeChoices.KITCHEN,
            ),
        )
        created_objs.append(
            self.create(
                order=order,
                printer_id=printer_client_id,
                type=CheckTypeChoices.CLIENT,
            ),
        )
        return created_objs
