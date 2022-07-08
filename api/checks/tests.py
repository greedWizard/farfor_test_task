from rest_framework import status
from rest_framework.test import APITestCase

from django.urls import reverse
from core.apps.checks.constants import CheckStatus, CheckTypeChoices

from core.apps.checks.models import Check


class ChecksAPITestCase(APITestCase):
    fixtures = [
        'core/apps/printers/fixtures/printers.json',
    ]

    @property
    def check_create_url(self):
        return reverse('api:checks:create_checks')

    def test_api_check_create_success(self):
        point_id = 1

        response = self.client.post(
            self.check_create_url,
            data={
                "id": 123456,
                "price": 780,
                "items": [
                {
                    "name": "Вкусная пицца",
                    "quantity": 2,
                    "unit_price": 250
                },
                {
                    "name": "Не менее вкусные роллы",
                    "quantity": 1,
                    "unit_price": 280
                }
                ],
                "address": "г. Уфа, ул. Ленина, д. 42",
                "client": {
                    "name": "Иван",
                    "phone": 9173332222
                },
                "point_id": point_id,
            },
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())
        self.assertTrue(
            Check.objects.filter(
                type=CheckTypeChoices.CLIENT,
                status=CheckStatus.NEW,
            ),
            'чек для клиента не создался',
        )
        self.assertTrue(
            Check.objects.filter(
                type=CheckTypeChoices.KITCHEN,
                status=CheckStatus.NEW,
            ),
            'чек для кухни не создался',
        )
