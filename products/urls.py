from django.urls import path
from . import  views

urlpatterns=[

    path('add_category', views.add_category, name='add_category'),
    path('list_category', views.list_category, name='list_category'),
    path('update_category/<id>/', views.update_category, name='update_category'),
    path('delete_category/<id>/', views.delete_category, name='delete_category'),

    path('add_origin', views.add_origin, name='add_origin'),
    path('list_origin', views.list_origin, name='list_origin'),
    path('update_origin/<id>/', views.update_origin, name='update_origin'),
    path('delete_origin/<id>/', views.delete_origin, name='delete_origin'),

    #path('add_seller', views.add_seller, name='add_seller'),
    path('add_product', views.add_product, name='add_product'),
    path('show_product', views.show_product, name='show_product'),
    path('update_product/<id>/', views.update_product, name='update_product'),
    path('delete_product/<id>/', views.delete_product, name='delete_product'),



]