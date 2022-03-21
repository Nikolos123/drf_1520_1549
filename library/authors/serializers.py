import datetime

from rest_framework import serializers


from .models import Author

class AuthorModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('first_name','last_name')
        # fields = ('first_name','las',)