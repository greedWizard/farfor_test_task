from django.db.models import Manager, QuerySet, Model

from core.apps.checks.constants import CheckTypeChoices


class PrinterQuerySet(QuerySet):
    def get_kitchen_printer(self, point_id: int) -> 'PrinterQuerySet':
        return self.filter(
            point_id=point_id,
            check_type=CheckTypeChoices.KITCHEN,
        ).first()

    def get_client_printer(self, point_id: int) -> 'PrinterQuerySet':
        return self.filter(
            point_id=point_id,
            check_type=CheckTypeChoices.CLIENT,
        ).first()


class PrinterManager(Manager):
    def get_queryset(self) -> PrinterQuerySet:
        return PrinterQuerySet(model=self.model, using=self._db)

    def get_kitchen_printer(self, **kwargs) -> Model:
        return self.get_queryset().get_kitchen_printer(**kwargs)

    def get_client_printer(self, **kwargs) -> Model:
        return self.get_queryset().get_client_printer(**kwargs)