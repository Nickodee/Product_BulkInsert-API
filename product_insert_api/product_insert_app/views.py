# views.py

from rest_framework import viewsets
from rest_framework.response import Response
from .models import Product, Product_Variant
from .serializers import ProductSerializer, ProductVariantSerializer

class ProductViewSet(viewsets.ViewSet):
    def create(self, request):
        products_data = request.data.get('products', [])
        products_serializer = ProductSerializer(data=products_data, many=True)
        if products_serializer.is_valid():
            products_serializer.save()
            return Response(products_serializer.data, status=201)
        return Response(products_serializer.errors, status=400)

    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

class ProductVariantViewSet(viewsets.ModelViewSet):
    queryset = Product_Variant.objects.all()
    serializer_class = ProductVariantSerializer
