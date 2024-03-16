# serializers.py

from rest_framework import serializers
from .models import Product, Product_Variant

class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Variant
        fields = ['sku', 'name', 'price', 'details']

class ProductSerializer(serializers.ModelSerializer):
    variants = ProductVariantSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'image', 'variants']

    def create(self, validated_data):
        variants_data = validated_data.pop('variants')
        product = Product.objects.create(**validated_data)
        for variant_data in variants_data:
            Product_Variant.objects.create(product_id=product, **variant_data)
        return product
