from django.conf import settings
from django.views.generic.base import TemplateView
from django.shortcuts import render
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=5000000,
            currency='inr',
            description='Donations',
            source=request.POST['stripeToken']
        )
        to_list = []
        for user in User.objects.filter(is_donor=True):
            to_list.append(user.email)
        for user in User.objects.filter(is_member=True):
            to_list.append(user.email)
        subject = 'Donations!!'
        message = 'Received donations!!'
        from_email = settings.EMAIL_HOST_USER
        to_list = to_list
        send_mail(subject, message, from_email, to_list, fail_silently = True)
        return render(request, 'charge.html')
