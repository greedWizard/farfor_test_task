from django.db.models import TextChoices


class CheckTypeChoices(TextChoices):
    KITCHEN = 'kichen', 'kitchen'
    CLIENT = 'client', 'client'


class CheckStatus(TextChoices):
    NEW = 'new', 'new'
    RENDERED = 'rendered', 'rendered'
    PRINTED = 'printed', 'printed'
