from django.urls import path
from .views import (
    ProductListCreateGenericAPIView,
    ProductDetailUpdateDeleteGenericAPIView
)

urlpatterns = [
    path('products/', ProductListCreateGenericAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailUpdateDeleteGenericAPIView.as_view(), name='product-detail-crud'),
]