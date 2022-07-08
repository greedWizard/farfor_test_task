from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from api.checks.serializers import CheckCreateSeriazlier
from core.apps.checks.models import Check


class ChecksAPIView(
    CreateModelMixin,
    GenericViewSet,
):
    queryset = Check.objects.all()
    serializer_class = CheckCreateSeriazlier

    def create(self, request, *args, **kwargs):
        serializer: CheckCreateSeriazlier = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if serializer.create_checks(serializer.validated_data):
            return Response(data={ 'ok': 'Чеки успешно созданы' })
        return Response(data={ 'error': 'Не удалось создать чеки' })
