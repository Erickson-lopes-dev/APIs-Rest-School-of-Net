from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Category


class CategorySerializer(serializers.ModelSerializer):
    # id do usuario
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    # nome do usuario
    user = serializers.StringRelatedField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'user']
        # mostrar todos
        # fields = '__all__'
