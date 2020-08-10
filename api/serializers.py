from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Category, Product


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


class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(read_only=True, many=True)
    categories_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(),
                                                       write_only=True,
                                                       source='categories')

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'categories', 'categories_id']
