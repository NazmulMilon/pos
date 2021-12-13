from django.contrib import admin
from .models import Category, Product, Country, Seller

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Country)
admin.site.register(Seller)
