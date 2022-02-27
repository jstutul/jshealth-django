from rest_framework import serializers
from service.models import *
from api.models import *

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'details', 'image', 'created']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name','image']


class ClientSaySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientSay
        fields = ['id', 'name','degisnation','image']


class AboutUSSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ['id', 'name','degisnation','image']