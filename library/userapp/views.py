from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView

from userapp.serializers import UserModelSerializer, UserFullModelSerializer


class UserListApiView(ListAPIView):
    queryset = User.objects.all()


    def get_serializer_class(self):
        if self.request.version == 'v2':
            return UserFullModelSerializer
        return UserModelSerializer

