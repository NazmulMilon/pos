from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pos_app.urls', namespace="pos_app")),
    path('', include('product.urls', namespace="product")),
]
