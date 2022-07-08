from typing import Any
from django.db.models import Manager, Model

from core.apps.checks.constants import CheckTypeChoices


class CheckManager(Manager):
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
