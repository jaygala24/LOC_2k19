from .forms import *
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model, authenticate, login, logout

User = get_user_model()

def register_view(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        password2 = request.POST['password2']
        name = first_name + " " + last_name
        if password == password2:
            if User.objects.filter(email__iexact=email).exists():
                return redirect('accounts:register')
            user = User.objects.create_user(
                email=email, name=name, phone=phone, password=password)
            user.save()
            return redirect('accounts:login')
        return redirect('accounts:register')
    return render(request, 'accounts/register.html')

def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts:dashboard')
        return redirect('accounts:login')
    return render(request, 'accounts/login.html')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:login')

