from typing import Any
from django.db.models import Manager, Model

from core.apps.checks.constants import CheckStatus, CheckTypeChoices


class CheckManager(Manager):
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
