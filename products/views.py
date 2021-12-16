from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Product, Category, Seller, Origin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
#from .models import *
# Create your views here.

# category details
def add_category(request):
    new_obj=Category()
    if request.method=="POST":
        new_obj.category_name=request.POST['category_name']
        #new_origin=Origin(origin_name)
        new_obj.save()
        messages.success(request, 'Origin has successfully done.')
        return redirect('list_category')
    return render(request, 'product/category/category_add.html')


def list_category(request):
    show_category=Category.objects.all()
    context={
        'categories': show_category
    }
    return render(request, 'product/category/category_list.html', context)

def update_category(request, id):
    update = Category.objects.get(id=id)
        
    if request.method=="POST":
        #  s=request.POST.get('category_name')
        # u=Category(category_name=s)

        update.category_name=request.POST.get('category_name')
        update.save()
        return redirect('list_category')

    context = {
        'categories': update
    }
    return render(request, 'product/category/category_update.html', context)

def delete_category(request, id):
    delete_obj=Category.objects.get(id=id)
    delete_obj.delete()
    return redirect('list_category')


#Origin_details.........
def add_origin(request):
    new_obj=Origin()
    if request.method=="POST":
        new_obj.origin_name=request.POST['origin_name']
        #new_origin=Origin(origin_name)
        new_obj.save()
        messages.success(request, 'Origin has successfully done.')
        return redirect('list_origin')
    return render(request, 'product/origin/origin_add.html')

def list_origin(request):
    show_origin=Origin.objects.all()
    context={
        'origins': show_origin
    }
    return render(request, 'product/origin/origin_list.html', context)


def update_origin(request, id):
    update = Origin.objects.get(id=id)
        
    if request.method=="POST":
        #  s=request.POST.get('category_name')
        # u=Category(category_name=s)

        update.origin_name=request.POST.get('origin_name')
        update.save()
        return redirect('list_origin')

    context = {
        'update_origin': update
    }
    return render(request, 'product/origin/origin_update.html', context)

def delete_origin(request, id):
    delete_object=Origin.objects.get(id=id)
    delete_object.delete()
    return redirect('list_origin')



# def add_seller(request):
#     seller=UserProfile.objects.all()
#     if request.method=="POST":
#         seller_id=request.POST.get('seller_name')
#         seller_name=UserProfile.objects.get(id=seller_id)
#         if Seller.objects.filter(seller_id=seller_id).exists():
#             return HttpResponse('Please Try another Seller')
#         else:
#             new_seller=Seller.objects.create(

#             seller_name=seller_name,

#             )
#             new_seller.save()
#             return HttpResponse('Your Product has successfully Added')
#     context={
#         'seller': seller,
#     }
#     return render(request, 'product/seller_add.html', context)



#Product_view
def add_product(request):
    category=Category.objects.all()
    seller=Seller.objects.all()
    origin=Origin.objects.all()
    if request.method=="POST":
        product_code=request.POST['product_code']
        product_name=request.POST['product_name']

        category_id=request.POST.get('product_category')
        product_category=Category.objects.get(id=category_id)
        #product_category=request.POST.get('product_category')

        product_quantity=request.POST['product_quantity']

        seller_id=request.POST.get('product_seller')
        product_seller=Seller.objects.get(id=seller_id)
        #product_seller=request.POST.get('product_seller')

        product_purchase_price=request.POST['product_purchase_price']
        product_selling_price=request.POST['product_selling_price']

        origin_id=request.POST.get('product_origin')
        product_origin=Origin.objects.get(id=origin_id)
        #product_origin=request.POST.get('product_origin')
        if Product.objects.filter(product_code=product_code).exists():
            return HttpResponse('This Product has already taken. Please Try another Product')
        else:
            Product.objects.create(
            product_code=product_code, 
            product_name=product_name,
            product_quantity=product_quantity, 
            product_purchase_price=product_purchase_price, 
            product_selling_price=product_selling_price,
            
            product_category=product_category,
            product_seller=product_seller,
            product_origin=product_origin,
            
            
            )
            # s=Category(category_name=product_category)
            # new_product.save()
            # s.save()
            #return HttpResponse('Your Product has successfully Added')
            return redirect('list_product')
    context={
        'categories': category,
        'sellers': seller,
        'origins': origin,
    }
    return render(request, 'product/product/product_add.html',context)
    

def list_product(request):
    show_product=Product.objects.all()
    context={
        'product': show_product
    }
    return render(request, 'product/product/product_list.html', context)


def update_product(request, id):
    update = Product.objects.get(id=id)
    categories=Category.objects.all()
    sellers=Seller.objects.all()
    origins=Origin.objects.all()

    if request.method=="POST":

        update.product_code=request.POST.get('product_code')
        update.product_name=request.POST.get('product_name')

        category_id=request.POST.get('product_category')
        prod_category=Category.objects.get(id=category_id)
        update.product_category=prod_category

        update.product_quantity=request.POST.get('product_quantity')

        seller_id=request.POST.get('product_seller')
        prod_seller=Seller.objects.get(id=seller_id)
        update.product_seller=prod_seller
        #u.product_seller=request.POST.get('product_seller')

        update.product_purchase_price=request.POST.get('product_purchase_price')
        update.product_selling_price=request.POST.get('product_selling_price')

        origin_id = request.POST.get('product_origin')
        prod_origin = Origin.objects.get(id=origin_id)
        update.product_origin = prod_origin

        update.save()
        return redirect('list_product')

    context = {
        'update': update,
        'categories':categories,
        'sellers':sellers,
        'origins': origins,
    }
    return render(request, 'product/product/product_update.html', context)


def delete_product(request, id):
    delete_object=Product.objects.get(id=id)
    delete_object.delete()
    return redirect('list_product')