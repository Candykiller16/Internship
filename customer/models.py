from django.contrib.auth.models import User
from django.db import models
from abstractions.abstact_models import Statuses, Info
from provider.models import Car


class Customer(Statuses, Info):
    """ Customer """

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    balance = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name


class CustomerOffer(models.Model):
    """ Customer's offer"""

    customer = models.ForeignKey(Customer, related_name="customers_offer", on_delete=models.CASCADE, null=True,
                                 blank=True)
    car = models.ForeignKey(Car, related_name="customers_cars_in_offer", on_delete=models.SET_NULL, null=True,
                            blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True,
                                help_text="<b>The price of the car specified when creating offer</b>")
