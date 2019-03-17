from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.core.mail import send_mail
from .forms import UserCreationForm, UserChangeForm
from donations.models import Donation

User = get_user_model()


def register_view(request):
    if request.method == "POST":
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        phone = request.POST.get('phone', None)
        password = request.POST.get('password', None)
        user = User.objects.create_volunteer(
            email=email, name=name, phone=phone, password=password)
        user.save()

        to_list = []
        for user in User.objects.all():
            to_list.append(user.email)
        subject = 'New Volunteer!!'
        message = 'A New Volunteer has registered.'
        from_email = settings.EMAIL_HOST_USER
        to_list = to_list
        send_mail(subject, message, from_email, to_list, fail_silently=True)

    return render(request, 'accounts/register.html', {'form': UserCreationForm})


def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        user = authenticate(email=email, password=password, is_member=True)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        context = {
            'error': 'Invalid Credentials'
        }
        return render(request, 'login.html', context)
    return render(request, 'login.html')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:login')


def members_data(request):
    members = User.objects.filter(is_member=True)
    context = {
        'members': members
    }
    return render(request, 'members.html', context)


def donors_data(request):
    donors = Donation.objects.all()
    context = {
        'donors': donors
    }
    return render(request, 'donors.html', context)


def volunteers_data(request):
    volunteers = User.objects.filter(is_volunteer=True)
    context = {
        'volunteers': volunteers,
    }
    return render(request, 'volunteers.html', context)


def volunteer_change_view(request, pk):
    if request.method == "POST":
        print(pk)
        user = get_object_or_404(User, pk=pk)
        if user is not None:
            user.is_active = not user.is_active
            user.save()
        return redirect('accounts:volunteers')
    return redirect('accounts:volunteers')
