from django.contrib.auth.models import User
from django.db import models
from abstract.models import Statuses, Info


class Customer(Statuses, Info):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    balance = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name
