import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django_countries.fields import CountryField
from django.utils import timezone


class Statuses(models.Model):
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def thirty_day_hence():
    return timezone.now() + timezone.timedelta(days=30)


class Discount(models.Model):
    bio = models.TextField(null=True)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=thirty_day_hence)
    discount_amount = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    amount = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        abstract = True


class Info(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    country = CountryField(multiple=True, blank=True)
    foundation_year = models.PositiveIntegerField(default=datetime.datetime.today().year,
                                                  help_text="<b>Year of foundation</b>",
                                                  null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True
