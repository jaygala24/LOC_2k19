from .forms import *
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model, authenticate, login, logout
from .forms import *

User = get_user_model()

def register_view(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        user = User.objects.create_user(
            email=email, name=name, phone=phone, password=password)
        user.save()

        to_list = []
        for user in User.objects.all():
            to_list.append(user.email)
        subject = 'New Volunteer!!'
        message = 'A New Volunteer has registered.'
        from_email = settings.EMAIL_HOST_USER
        to_list = to_list
        send_mail(subject, message, from_email, to_list, fail_silently = True)

    return render(request, 'accounts/register.html', {'form': UserCreationForm})

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

