# Generated by Django 4.0.6 on 2022-07-19 12:11

import abstractions.abstact_models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('showroom', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=746, multiple=True)),
                ('foundation_year', models.PositiveIntegerField(blank=True, default=2022, help_text='<b>Year of foundation</b>', null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('percentage_of_price_increase', models.PositiveIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'provider',
            },
        ),
        migrations.CreateModel(
            name='DiscountProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(null=True)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(default=abstractions.abstact_models.thirty_day_hence)),
                ('discount_amount', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('amount', models.PositiveIntegerField(blank=True, null=True)),
                ('provider', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='provider_discounts', to='provider.provider')),
            ],
            options={
                'db_table': 'provider_discount',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('model', models.CharField(blank=True, help_text="Car's model", max_length=50, null=True)),
                ('body_type', models.CharField(choices=[('1', "Car's body type"), ('2', 'Hatchback'), ('3', 'Minivan'), ('4', 'CrossOverVehicle'), ('5', 'Coupe'), ('6', 'Supercar'), ('7', 'Cabriolet'), ('8', 'Sedan'), ('9', 'Micro')], default='1', max_length=20)),
                ('transmission_type', models.CharField(choices=[('1', 'Automation'), ('2', 'Mechanics')], default='2', max_length=20)),
                ('color', models.CharField(blank=True, help_text="<b>Car's color</b>", max_length=50, null=True)),
                ('year', models.PositiveIntegerField(blank=True, default=2022, help_text='<b>Year of production</b>', null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, help_text="<b>Car's weight in kilograms</b>", max_digits=5, null=True)),
                ('acceleration', models.DecimalField(blank=True, decimal_places=1, help_text="<b>Car's acceleration to 100 km per hour</b>", max_digits=2, null=True)),
                ('average_fuel_consumption', models.DecimalField(decimal_places=1, help_text="<b>Car's average fuel consumption per 100 km</b>", max_digits=2)),
                ('bio', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, help_text='<b>The initial price of the car</b>', max_digits=5, null=True)),
                ('provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='providers_cars', to='provider.provider')),
                ('showroom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='showrooms_cars', to='showroom.showroom')),
            ],
            options={
                'db_table': 'car',
            },
        ),
    ]
