from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Category


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']
        # fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    # id do usuario
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    # nome do usuario
    # user = serializers.StringRelatedField()

    # instância de um serializer - GET
    user = UserSerializer(read_only=True)

    # exibir apenas para escrita - POST/PUT
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),
                                                 write_only=True,
                                                 # nome do campo em models
                                                 source='user')

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'user', 'user_id']
        # mostrar todos
        # fields = '__all__'
