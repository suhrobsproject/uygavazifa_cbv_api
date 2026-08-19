from rest_framework import generics, mixins
from drf_yasg.utils import swagger_auto_schema
from .models import Product
from .serializers import ProductSerializer


class ProductListCreateGenericAPIView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @swagger_auto_schema(operation_description="Barcha mahsulotlar ro'yxatini olish")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Yangi mahsulot yaratish")
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductDetailUpdateDeleteGenericAPIView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    @swagger_auto_schema(operation_description="Bitta mahsulot tafsilotini ko'rish")
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Mahsulotni to'liq yangilash (PUT)")
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Mahsulotni qisman yangilash (PATCH)")
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Mahsulotni o'chirish (DELETE)")
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)