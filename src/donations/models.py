from django.db import models
from . import choices

# Create your models here.

class Donations(models.Model):
    amount = models.PositiveIntegerField(default=0)
    date_time = models.DateTimeField(auto_now_add = True)
    mode_of_payment = models.CharField(max_length = 2, choices = choices.Mode_Of_Payment)