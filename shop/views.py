from rest_framework import viewsets, mixins
from .models import Cart, Category
from .serializers import CartSerializer, CategorySerializer
from rest_framework.response import Response


class ShopViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def list(self, request, *args, **kwargs):
        all_cart = Cart.objects.all()
        serializer_cart = CartSerializer(all_cart, many=True, context={'request': request})
        all_category = Category.objects.all()
        serializer_category = CategorySerializer(all_category, many=True, context={'request': request})
        return Response(serializer_cart.data + serializer_category.data)


