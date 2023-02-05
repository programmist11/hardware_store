from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'', views.ShopViewSet, basename="cart")


urlpatterns = [
    path('category/<int:category_id>', views.CategoryListAPIView.as_view(), name='category'),
    path('', views.ShopViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:cart_id>', views.ShopViewSet.as_view({'get': 'retrieve'})),
]

