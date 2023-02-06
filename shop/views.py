from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Cart, Category
from .serializers import CartSerializer, CategorySerializer, PhoneSerializer
from .service import send_massage


class ShopViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def create(self, request):
        serializer = PhoneSerializer(data=request.data)

        if serializer.is_valid():
            phone = serializer.validated_data.get("phone")
            name = serializer.validated_data.get("name")
            send_massage(phone, name)
            return Response(status=200)
        return Response(status=400)


class CategoryRetrieveAPIView(APIView):

    def get(self, request, *args, **kwargs):

        category_id = kwargs.get("category_id")
        category = get_object_or_404(Category, pk=category_id)
        queryset = category.cart_set.all()

        serializer = CartSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)


class CategoryListAPIView(APIView):

    def get(self, request, *args, **kwargs):

        queryset = Category.objects.all()

        serializer = CategorySerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)


