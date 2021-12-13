from django.urls import path
from .import views

app_name='product'

urlpatterns = [
    path('create-category/', views.CategoryCRUDView.as_view(), name='create_category_url'),
    path('category-list/', views.CategoryListView.as_view(), name='category_list_url'),


    path('create-country/', views.CountryCRUDView.as_view(), name='create_country_url'),
    path('country-list/', views.CountryListView.as_view(), name='country_list_url'),


    path('create-seller/', views.SellerCRUDView.as_view(), name='create_seller_url'),
    path('seller-list/', views.SellerListView.as_view(), name='seller_list_url'),

    path('create-product/', views.ProductCRUDView.as_view(), name='create_product_url'),
    path('product-list/', views.ProductListView.as_view(), name='product_list_url'),

]
