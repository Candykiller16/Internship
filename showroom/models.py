from django.contrib.auth.models import User
from django.db import models
from abstractions.abstact_models import Statuses, Info, Discount


class Showroom(Statuses, Info):
    """ Showroom """

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

    class Meta:
        db_table = "showroom"

    def str(self):
        return f"{self.name}"


class DiscountShowroom(Statuses, Discount):
    """ Showroom Discount"""

    showroom = models.ForeignKey(
        Showroom,
        on_delete=models.PROTECT,
        related_name="showroom_discount",
        null=True,
        verbose_name="showroom",
    )

    class Meta:
        db_table = "showroom_discount"

    def str(self):
        return f"{self.start_date} {self.end_date} {self.discount_amount} {self.showroom}"
