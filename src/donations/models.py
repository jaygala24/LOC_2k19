import datetime
from django.db.models import Func
from django.db import models
from django.db.models import Sum, Q
from django.contrib.auth import get_user_model
from . import choices

User = get_user_model()


class Donor(models.Model):
    email = models.EmailField(
        max_length=255, unique=True, verbose_name='email address')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Month(Func):
    function = 'EXTRACT'
    template = '%(function)s(MONTH from %(expressions)s)'
    output_field = models.IntegerField()


class DonationManager(models.Manager):
    def total(self, *args, **kwargs):
        sum = 0
        donations = Donation.objects.all()
        for donation in donations:
            sum += donation.amount
        return sum

    def analysis(self, *args, **kwargs):
        day = datetime.datetime.now()
        prev_day = day - datetime.timedelta(365)
        dates_Arr = [prev_day]
        for i in range(1, 13):
            dates_Arr.append(dates_Arr[i-1] + datetime.timedelta((365/12)))
        summary = []
        for i in range(1, len(dates_Arr)):
            prev = dates_Arr[i-1]
            next = dates_Arr[i]
            donations = Donation.objects.filter(
                Q(timestamp__gte=prev) & Q(timestamp__lte=next))
            sum = 0
            for donation in donations:
                sum += donation.amount
            myDict = {
                'month': prev.month,
                'year': prev.year,
                'amount': sum
            }
            summary.append(myDict)
        return summary


class Donation(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    mode_of_payment = models.CharField(
        max_length=2, choices=choices.Mode_Of_Payment)

    objects = DonationManager()

    def __str__(self):
        return f"{self.donor} - {self.amount}"
