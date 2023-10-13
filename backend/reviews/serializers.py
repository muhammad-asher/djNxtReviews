from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'


class BusinessSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Business
        fields = '__all__'


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'
