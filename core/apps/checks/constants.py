from django.db.models import TextChoices


class CheckTypeChoices(TextChoices):
    KITCHEN = 'kitchen', 'кухня'
    CLIENT = 'client', 'клиент'


class CheckStatus(TextChoices):
    NEW = 'new', 'новый'
    RENDERED = 'rendered', 'готов к печати'
    PRINTED = 'printed', 'напечатан'
