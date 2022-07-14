from django.contrib import admin
from .models import Car, Provider, DiscountProvider

admin.site.register(Car)
admin.site.register(Provider)
admin.site.register(DiscountProvider)
