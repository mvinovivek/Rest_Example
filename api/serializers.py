from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from.models import Note

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Note
        fields="__all__"