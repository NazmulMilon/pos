from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(request):
    return render(request, 'index.html')

def registration(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        user_name=request.POST['user_name']
        email=request.POST['email']
        password=request.POST['password']
        phone=request.POST['phone']
        if User.objects.filter(username=user_name).exists():
            return HttpResponse('This Username has already taken. Please Try another name.')
        else:
            new_user=User(first_name=first_name, last_name=last_name, username=user_name, email=email, password=password)
            new_user.save()

            new_profile=UserProfile(user=new_user, phone=phone)
            new_profile.save()
            return HttpResponse('Your Registration has successfully done')
    return render(request, 'registration.html')

# def update_user(request, id):
#     u = UserProfile.objects.get(id=id)
#     user_obj=UserProfile.objects.all()

#     if request.method=="POST":

#         u.first_name=request.POST.get('first_name')
#         u.last_name=request.POST.get('last_name')
#         u.user_name=request.POST.get('user_name')
#         u.email=request.POST.get('email')
#         u.password=request.POST.get('password')
#         u.phone=request.POST.get('phone')

#         u.save()

#     context = {
#         'get_object': u,
#         'user_object':user_obj,

#     }
#     return render(request, 'update_user.html', context)


def user_login(request):
    if request.method=="POST":
        user_name=request.POST['user_name']
        password=request.POST['password']
        user=authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            #return HttpResponse('Your Login has successfully done.')
            return redirect('/')
        else:
            return HttpResponse('Wrong Username or Password')

    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('/')

