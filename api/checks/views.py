from django.http import HttpResponse

from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from api.checks.filters import CheckFilter
from api.checks.serializers import CheckCreateSeriazlier, CheckListSerializer
from core.apps.checks.models import Check


class ChecksAPIView(
    RetrieveModelMixin,
    ListModelMixin,
    CreateModelMixin,
    GenericViewSet,
):
    queryset = Check.objects.avaliable_for_printing()
    serializer_class = CheckCreateSeriazlier
    filterset_class = CheckFilter

    def retrieve(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        check: Check = queryset.first()

        if not check:
            return HttpResponse(content=b'')
        response = HttpResponse(content=check.pdf_file.read())
        response['Content-Disposition'] = f'attachment; filename="{check.pdf_file.name}"'
        return response 

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        avaliable_for_printing_ids = queryset.values_list('id', flat=True)

        list_serializer = CheckListSerializer(
            data={
                'checks': avaliable_for_printing_ids,
            }
        )
        list_serializer.is_valid(raise_exception=True)
        return Response(data=list_serializer.data)

    def create(self, request, *args, **kwargs):
        serializer: CheckCreateSeriazlier = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if serializer.create_checks(serializer.validated_data):
            return Response(data={ 'ok': 'Чеки успешно созданы' })
        return Response(data={ 'error': 'Не удалось создать чеки' })
