from rest_framework import serializers

from .models import Cart, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Category


class CartSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        # fields = "__all__"
        fields = ('id', 'title', 'descriptions', 'category', 'photo', 'price')
        model = Cart


class PhoneSerializer(serializers.Serializer):
    phone = serializers.CharField()
    name = serializers.CharField()
