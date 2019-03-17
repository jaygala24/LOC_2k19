from django.conf import settings
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth import get_user_model, authenticate, login, logout
from .models import Donation, Donor
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

User = get_user_model()


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=200000,
            currency='inr',
            description='Donation',
            source=request.POST['stripeToken']
        )

        to_list = []
        for donor in Donor.objects.all():
            to_list.append(donor.email)
        for user in User.objects.filter(is_member=True):
            to_list.append(user.email)
        subject = 'Donations!!'
        message = 'Received donations!!'
        from_email = settings.EMAIL_HOST_USER
        to_list = to_list
        send_mail(subject, message, from_email, to_list, fail_silently = True)

        return render(request, 'charge.html', {'amount': amount})
