from django.urls import path, include
from rest_framework.routers import DefaultRouter

from onfido.views import ProfileViewSet

app_name = 'onfido'

router = DefaultRouter()
router.register('', ProfileViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
