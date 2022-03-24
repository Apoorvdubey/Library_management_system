from pyexpat import model
from rest_framework.serializers import ModelSerializer
from .models import *



class BookListSerializer(ModelSerializer):

    class Meta:
        model= Book
        fields = "__all__"