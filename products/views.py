from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Product,Category, Seller, Origin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from .models import *
# Create your views here.


def add_product(request):
    cat=Category.objects.all()

    sell=Seller.objects.all()
    ori=Origin.objects.all()
    if request.method=="POST":
        product_code=request.POST['product_code']
        product_name=request.POST['product_name']
        product_category=request.POST.get('product_category')
        product_quantity=request.POST['product_quantity']
        product_seller=request.POST.get('product_seller')
        product_purchase_price=request.POST['product_purchase_price']
        product_selling_price=request.POST['product_selling_price']
        product_origin=request.POST.get('product_origin')
        if Product.objects.filter(product_code=product_code).exists():
            return HttpResponse('This Product has already taken. Please Try another Product')
        else:
            new_product=Product(
            product_code=product_code, 
            product_name=product_name,
            product_quantity=product_quantity, 
            product_purchase_price=product_purchase_price, 
            product_selling_price=product_selling_price,
            product_category=product_category,
            product_seller=product_seller,
        
            product_origin=product_origin,
            
            
            )
            new_product.save()
            return HttpResponse('Your Product has successfully Added')
    con={
        'c': cat,
        's': sell,
        'o': ori,
    }
    return render(request, 'product/product_add.html',con)
    


# def add_product(request):
#     ori=Origin.objects.all()
#     if request.method=="POST":
#         if request.POST.get('origin_name'):
#             saveorigin=Product()
#             saveorigin.origin_name=request.POST.get('origin_name')
#             saveorigin.save()
#             messages.success(request, 'Data has saved successfully')
#             #return render(request, 'index.html')
#     context={

#         'o': ori,
#     }
    
#     return render(request, 'product_add.html', context)
