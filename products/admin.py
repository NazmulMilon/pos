from django.contrib import admin
from .models import Category, Origin, Seller, Product
# Register your models here.
admin.site.register(Category)
admin.site.register(Origin)
admin.site.register(Seller)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_code', 'product_name', 'product_category','product_seller', 'product_purchase_price', 'product_selling_price', 'product_origin')
    #list_filter = ['product_category', 'product_name']
admin.site.register(Product, ProductAdmin)


