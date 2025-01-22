# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Customer(models.Model):

    #__Customer_FIELDS__
    first name = models.TextField(max_length=255, null=True, blank=True)
    last name = models.TextField(max_length=255, null=True, blank=True)
    phone = models.TextField(max_length=255, null=True, blank=True)
    e-mail = models.TextField(max_length=255, null=True, blank=True)
    address 1 = models.TextField(max_length=255, null=True, blank=True)

    #__Customer_FIELDS__END

    class Meta:
        verbose_name        = _("Customer")
        verbose_name_plural = _("Customer")


class Bike(models.Model):

    #__Bike_FIELDS__
    model = models.TextField(max_length=255, null=True, blank=True)
    vin = models.TextField(max_length=255, null=True, blank=True)
    mileage = models.TextField(max_length=255, null=True, blank=True)
    status = models.TextField(max_length=255, null=True, blank=True)

    #__Bike_FIELDS__END

    class Meta:
        verbose_name        = _("Bike")
        verbose_name_plural = _("Bike")



#__MODELS__END
