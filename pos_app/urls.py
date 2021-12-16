from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('registration', views.registration, name='registration'),
    #path('update_user/<id>/', views.update_user, name='update_user'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),

]