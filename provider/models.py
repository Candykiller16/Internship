from django.db import models
from django.db.models.functions import datetime
from abstract.models import Statuses, Info, Discount
from django.contrib.auth.models import User
from showroom.models import Showroom

BODY_TYPES = [
    ('1', "Car's body type"),
    ('2', 'Hatchback'),
    ('3', 'Minivan'),
    ('4', 'CrossOverVehicle'),
    ('5', 'Coupe'),
    ('6', 'Supercar'),
    ('7', 'Cabriolet'),
    ('8', 'Sedan'),
    ('9', 'Micro'),

]

TRANSMISSION = [
    ('1', 'Automation'),
    ('2', 'Mechanics'),
]


class Car(Statuses):
    name = models.CharField(max_length=250, null=True, blank=True)
    model = models.CharField(max_length=50, null=True, blank=True, help_text="Car's model")
    body_type = models.CharField(max_length=20,
                                 choices=BODY_TYPES,
                                 default='1')
    transmission_type = models.CharField(max_length=20,
                                         choices=TRANSMISSION,
                                         default='2')
    color = models.CharField(max_length=50, help_text="<b>Car's color</b>", null=True, blank=True)
    year = models.PositiveIntegerField(default=datetime.datetime.today().year, help_text="<b>Year of production</b>",
                                       null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2,
                                 help_text="<b>Car's weight in kilograms</b>", null=True, blank=True)
    acceleration = models.DecimalField(max_digits=2, decimal_places=1,
                                       help_text="<b>Car's acceleration to 100 km per hour</b>", null=True, blank=True)
    average_fuel_consumption = models.DecimalField(max_digits=2, decimal_places=1,
                                                   help_text="<b>Car's average fuel consumption per 100 km</b>")
    bio = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    showroom = models.ForeignKey(
        Showroom,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="showrooms_cars",
    )

    class Meta:
        db_table = "car"

    def str(self):
        return f"{self.name} {self.model}"


class Provider(Info, Statuses):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    number_of_buyers = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        db_table = "provider"

    def str(self):
        return f"{self.name} {self.bio}"


class DiscountProvider(Discount):
    provider = models.ForeignKey(
        Provider,
        related_name="provider_discounts",
        on_delete=models.CASCADE,
        null=True,
    )

    class Meta:
        db_table = "provider_discount"

    def str(self):
        return f"{self.start_date} {self.end_date} {self.discount_amount} {self.provider}"
