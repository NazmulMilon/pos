from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from .models import Category, Product, Country, Seller

# Create your views here.
class CategoryCRUDView(View):    
    def get(self, request):                
        return render(request, 'category/create_category.html')
    
    def post(self, request):
        data_dict = dict()
        category_name = request.POST.get('category_name')
        data_dict['category_name'] = category_name
        category_obj = Category.objects.create(**data_dict)
        category_obj.save()
        return redirect('product:category_list_url')


class CategoryListView(View):    
    def get(self, request):        
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'category/category_list.html', context)


class CountryCRUDView(View):
    def get(self, request):
        return render(request, 'country/create_country.html')
    
    def post(self, request):
        data_dict = dict()
        country_name = request.POST.get('country_name')
        data_dict['country_name'] = country_name
        country_obj = Country.objects.create(**data_dict)     
        country_obj.save()          
        return redirect('product:country_list_url')


class CountryListView(View):
    def get(self, request):        
        countries = Country.objects.all()
        context = {
            'countries': countries
        }
        return render(request, 'country/country_list.html', context)



class SellerCRUDView(View):
    def get(self, request):
        return render(request, 'seller/create_seller.html')

    def post(self, request):
        data_dict = dict()
        seller_name = request.POST.get('seller_name')
        data_dict['seller_name'] = seller_name
        seller_obj = Seller.objects.create(**data_dict)
        seller_obj.save()
        return redirect('product:seller_list_url')

class SellerListView(View):
    def get(self, request):        
        sellers = Seller.objects.all()        
        context = {
            'sellers': sellers
        }
        return render(request, 'seller/seller_list.html', context)



class ProductCRUDView(View):
    def get(self, request):
        categories = Category.objects.all()         
        countries = Country.objects.all()   
        sellers = Seller.objects.all()      
        context = {
            'categories': categories,
            'countries': countries,
            'sellers': sellers
        }
        return render(request, 'product/create_product.html', context)
    
    def post(self, request):
        data_dict = dict()
        product_name = request.POST.get('product_name')
        product_code = request.POST.get('product_code')
        product_purchase_price = request.POST.get('product_purchase_price')
        product_selling_price = request.POST.get('product_selling_price')

        category_id = request.POST.get('category')
        category = Category.objects.get(id=category_id)

        country_id = request.POST.get('country')
        country = Country.objects.get(id=country_id)

        seller_id = request.POST.get('seller')
        seller = Seller.objects.get(id=seller_id)

        data_dict['product_name'] = product_name
        data_dict['product_code'] = product_code
        data_dict['product_purchase_price'] = product_purchase_price
        data_dict['product_selling_price'] = product_selling_price
        data_dict['category'] = category
        data_dict['country'] = country
        data_dict['seller'] = seller


        product_obj = Product.objects.create(**data_dict)
        product_obj.save()
        return redirect('product:product_list_url')
        



class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        context = {
            'products': products
        }
        return render(request, 'product/product_list.html', context)