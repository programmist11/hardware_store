import os

from rest_framework import viewsets, mixins
from .models import Cart, Category
from .serializers import CartSerializer, CategorySerializer, PhoneSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .service import send_massage


class ShopViewSet(viewsets.ViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def list(self, request):

        all_cart = Cart.objects.all()
        serializer_cart = CartSerializer(all_cart, many=True, context={'request': request})
        all_category = Category.objects.all()
        serializer_category = CategorySerializer(all_category, many=True, context={'request': request})
        return Response(serializer_cart.data + serializer_category.data)

    def create(self, request):
        serializer = PhoneSerializer(data=request.data)

        if serializer.is_valid():
            phone = serializer.validated_data.get("phone")
            name = serializer.validated_data.get("name")
            send_massage(phone, name)
            return Response(status=200)
        return Response(status=400)

    def retrieve(self, request, cart_id):
        cart = get_object_or_404(Cart, pk=cart_id)
        serializer = CartSerializer(cart, many=False, context={'request': request})
        return Response(serializer.data)



class CategoryListAPIView(APIView):

    def get(self, request, *args, **kwargs):

        category_id = kwargs.get("category_id")
        category = get_object_or_404(Category, pk=category_id)
        category_cart = category.cart_set.all()

        serializer_category_cart = CartSerializer(category_cart, many=True, context={'request': request})
        serializer_category = CategorySerializer(category, many=False, context={'request': request})
        print(serializer_category_cart.data)
        print(serializer_category.data)

        return Response(serializer_category_cart.data + serializer_category.data)




