from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Country(models.Model):
    country_name = models.CharField(max_length=100)

    def __str__(self):
        return self.country_name
    
class Seller(models.Model):
    seller_name = models.CharField(max_length=100)

    def __str__(self):
        return self.seller_name
    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    product_name = models.CharField(max_length=50)
    product_code = models.CharField(max_length=20)
    product_purchase_price = models.IntegerField()
    product_selling_price = models.IntegerField()

    def __str__(self):
        return self.product_name


    