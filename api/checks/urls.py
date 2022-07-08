from django.urls import path

from api.checks.views import ChecksAPIView


urlpatterns = [
    path('create_checks', ChecksAPIView.as_view({
        'post': 'create',
    }), name='create_checks')
]
