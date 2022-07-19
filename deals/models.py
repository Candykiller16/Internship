from django.db import models
from provider.models import Provider, Car, DiscountProvider
from showroom.models import Showroom, DiscountShowroom
from customer.models import Customer


class FromProviderToShowroomDeal(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.PROTECT)
    showroom = models.ForeignKey(Showroom, on_delete=models.PROTECT)
    car = models.ForeignKey(Car, on_delete=models.PROTECT)
    providers_discount = models.ForeignKey(DiscountProvider, on_delete=models.PROTECT)

    class Meta:
        db_table = "sales_provider_to_showroom"

    def str(self):
        return f" From {self.provider} to {self.showroom} sold {self.car}"


class FormShowroomToCustomerDeal(models.Model):
    showroom = models.ForeignKey(Showroom, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    car = models.ForeignKey(Car, on_delete=models.PROTECT)
    showroom_discount = models.ForeignKey(DiscountShowroom, on_delete=models.PROTECT)

    class Meta:
        db_table = "sales_showroom_to_customer"

    def str(self):
        return f" From {self.showroom} to {self.customer} sold {self.car}"
