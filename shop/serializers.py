from rest_framework import serializers
from .models import Cart, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Category


class CartSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        fields = "__all__"
        model = Cart


class PhoneSerializer(serializers.Serializer):
    phone = serializers.CharField()
    name = serializers.CharField()
