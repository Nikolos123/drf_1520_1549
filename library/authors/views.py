from rest_framework import serializers
from rest_framework.decorators import api_view, renderer_classes

from rest_framework.renderers import JSONRenderer, AdminRenderer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser,BasePermission


from .models import Author, Biography, Book
from .serializers import AuthorModelSerializer, BiographyModelSerializer, BookModelSerializer, AuthorBaseModelSerializer


class StaffOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class AuthorModelViewSet(ModelViewSet):
    # renderer_classes = [AdminRenderer]
    # permission_classes = [StaffOnly]
    queryset = Author.objects.all()
    # serializer_class = AuthorModelSerializer

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return AuthorBaseModelSerializer
        return AuthorModelSerializer

class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer

class BookModelViewSet(ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    # parser_classes = [JSONParser]

    # def create(self, request, *args, **kwargs):
    #     pass