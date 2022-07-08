from django_filters import rest_framework as drf_filters

from core.apps.checks.models import Check


class CheckFilter(drf_filters.FilterSet):
    api_key = drf_filters.UUIDFilter(field_name='printer__api_key', required=True)
    check_id = drf_filters.NumberFilter(field_name='id')

    class Meta:
        model = Check
        fields = ('api_key', )
