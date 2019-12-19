from rest_framework import mixins, viewsets

from onfido.models import User
from onfido.serializers import UserSerializer


class ProfileViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
