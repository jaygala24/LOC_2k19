from django.shortcuts import render
from .forms import *

# Create your views here.

def signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        name = first_name + " " + last_name
        user = User.objects.create_user(
            email=email, name=name, phone=phone, password=password)
        user.save()
        subject = 'Account Verfication'
        from_email = settings.EMAIL_HOST_USER
        to_list = [email, from_email, ]
        msg = EmailMessage(subject, message, to=to_list,
                            from_email=from_email)
        msg.content_subtype = 'html'
        msg.send()
        messages.success(
            request, 'Email is sent for account verification')
    return render(request, 'index.html', {'form': UserCreationForm})