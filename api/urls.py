from django.urls import include, path


urlpatterns = [
    path('', include(('api.checks.urls', 'checks'), namespace='checks'))
]
