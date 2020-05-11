from django.db import models
import datetime
from django.utils.timezone import now
# Create your models here.


class Order(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    date = models.DateField(default=datetime.datetime.now)
    title = models.CharField(max_length=100,default='Order')
    price = models.DecimalField(max_digits=15,decimal_places=2, default=0)
    order_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=220, unique=True, default='')
    PAYMENT_METHOD = (
        ('NO','Choose'),
        ('CR', 'Card'),
        ('CS', 'Cash'),
        ('CH', 'Check'),
    )
    payment_method = models.CharField(max_length=2, choices=PAYMENT_METHOD, default='NO')


"""class Contact(models.Model):
    name = models.CharField(max_length=120, default='')
    email = models.EmailField(max_length=220, unique=True, default='')
    subject = models.CharField(max_length=100, default='')
    message = models.CharField(max_length=250, default='')
    contacted = models.BooleanField("Contacted", default=False)

    def __str__(self):
        return self.name
"""


class Sponsor(models.Model):
    name = models.CharField(max_length=120, default='')
    email = models.EmailField(max_length=220, unique=True, default='')
    subject = models.CharField(max_length=100, default='SponsorShip')
    contacted = models.BooleanField("Sponsor", default=False)

    def __str__(self):
        return self.name
