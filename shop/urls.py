from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'', views.ShopViewSet, basename="cart")


urlpatterns = [
    path('category/<int:category_id>', views.CategoryRetrieveAPIView.as_view(), name='category-detail'),
    path('category/', views.CategoryListAPIView.as_view(), name='category-list'),
]

urlpatterns += router.urls