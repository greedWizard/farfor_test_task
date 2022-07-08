from rest_framework import serializers
from rest_framework.serializers import Serializer

from core.apps.checks.services import create_checks

# Лень писать отдельные сериализатор под каждый вложенный объект, по этому пусть
# останутся json'ами
class CheckCreateSeriazlier(Serializer):
    id = serializers.IntegerField()
    items = serializers.ListField(child=serializers.JSONField())
    price = serializers.FloatField()
    client = serializers.JSONField()
    point_id = serializers.IntegerField()

    def create_checks(self, validated_data):
        return create_checks(json_data=validated_data)

    class Meta:
        fields = '__all__'
