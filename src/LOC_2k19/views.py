from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from donations.models import Donation, Donor

User = get_user_model()


def index(request):
    volunteer_count = User.objects.filter(is_volunteer=True).count()
    members_count = User.objects.filter(is_member=True).count()
    donors_count = Donor.objects.all().count()
    donations = Donation.objects.analysis()
    total = Donation.objects.total()
    context = {
        'volunteer': volunteer_count,
        'members': members_count,
        'donors': donors_count,
        'total': total,
        'donations': donations
    }
    return render(request, 'index.html', context)
