from django.urls import path

from api.checks.views import ChecksAPIView


urlpatterns = [
    path('create_checks', ChecksAPIView.as_view({
        'post': 'create',
    }), name='create_checks'),
    path('new_checks', ChecksAPIView.as_view({
        'get': 'list',
    }), name='new_checks'),
    path('check', ChecksAPIView.as_view({
        'get': 'retrieve',
    }), name='check'),
]
