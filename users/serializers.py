from dataclasses import field
from django.conf import UserSettingsHolder
from rest_framework.serializers import ModelSerializer
from . models import *

class UserListSerializer(ModelSerializer):

    class Meta:
        model = Users
        fields = "__all__"