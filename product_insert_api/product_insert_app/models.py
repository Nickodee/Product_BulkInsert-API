from django.db import models

# Create your models here.
#create the product model
class Product (models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)


#create the product variant model
class Product_Variant (models.Model):
    sku = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.CharField(max_length=255)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')