import datetime

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer


from .models import Author, Biography, Book


class AuthorModelSerializer(ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'

class AuthorBaseModelSerializer(ModelSerializer):

    class Meta:
        model = Author
        fields = ('last_name',)



class BiographyModelSerializer(ModelSerializer):

    class Meta:
        model = Biography
        fields = '__all__'


class BookModelSerializer(ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'