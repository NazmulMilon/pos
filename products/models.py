from django.db import models
from django.contrib.auth.models import User
#from django.db import Seller
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=10)

    def __str__(self):
        return self.category_name


class Origin(models.Model):
    origin_name = models.CharField(max_length=10,default=1)
    
    def __str__(self):
        return self.origin_name


class Seller(models.Model):
    seller_name = models.OneToOneField(User, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.seller_name.username


class Product(models.Model):
    product_code = models.CharField(max_length=20)
    product_name = models.CharField(max_length=20)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True,related_name='cat',blank=True)
    product_quantity = models.PositiveBigIntegerField(null=True)
    product_seller = models.ForeignKey(Seller, on_delete=models.CASCADE,null=True,related_name='seller',blank=True)
    product_purchase_price =models.PositiveIntegerField(null=True)
    product_selling_price = models.PositiveIntegerField(null=True)
    product_origin = models.ForeignKey(Origin, on_delete=models.CASCADE,null=True,related_name='origin',blank=True)
    #product_image = m
    #profit_percentage = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.product_name
