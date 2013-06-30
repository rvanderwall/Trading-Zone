# models.py
__author__ = 'robertv'
__copyright__ = "QED Testing, Inc. 2013"

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from message_strings import help_name, help_address

#TODO - Globalize help strings and units.

class Customer(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=30, help_text= help_name)
    address = models.CharField(max_length=100, help_text= help_address)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50, blank=True)
    active = models.BooleanField()
    email = models.EmailField()
    creation_date = models.DateField(blank=True, null=True)
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('customer')
        verbose_name_plural = _('customer')
        ordering = ['name']


class ChemicalPoolTest(models.Model):
    customer = models.ForeignKey(Customer)
    date_of_test = models.DateField(blank=False)

    ph = models.DecimalField(max_digits=2, decimal_places=2, blank=True, help_text="0 - 10.0")
    acid_demand = models.DecimalField(max_digits=3, decimal_places=0, blank=True, help_text="0-99 cups")
    chlorine_level = models.DecimalField(max_digits=4, decimal_places=2, blank=True, help_text="color based")
    bromine_level = models.DecimalField(max_digits=4, decimal_places=2, blank=True, help_text="color based")
    alkalinity = models.DecimalField(max_digits=4, decimal_places=2, blank=True, help_text="0-99.0")
    hardness = models.DecimalField(max_digits=4, decimal_places=2, blank=True, help_text="0-99.0")

    notes = models.CharField(max_length=500, blank=True)

    def __unicode__(self):
        return self.customer.name + self.date_of_test

    class Meta:
        ordering = ['-date_of_test']


class PoolMaintenance(models.Model):
    customer = models.ForeignKey(Customer)
    date_of_work = models.DateField(blank=False)

    acid = models.DecimalField(max_digits=3, decimal_places=0, blank=True, help_text="0-999 cups")
    liquid_chlorine = models.DecimalField(max_digits=3, decimal_places=2, blank=True, help_text="0-99 gallons")
    chlorine_shock = models.DecimalField(max_digits=3, decimal_places=2, blank=True, help_text="0-99 bags")
    bicarb = models.DecimalField(max_digits=3, decimal_places=2, blank=True, help_text="0-99 pounds")
    soda_ash = models.DecimalField(max_digits=3, decimal_places=2, blank=True, help_text="0-99 pounds")
    stabilizer = models.DecimalField(max_digits=3, decimal_places=2, blank=True, help_text="0-99 pounds")
    salt = models.DecimalField(max_digits=3, decimal_places=2, blank=True, help_text="0-999 pounds")
    brush_time = models.DecimalField(max_digits=3, decimal_places=2, blank=True, help_text="0-999 minutes")
    vacuum_time = models.DecimalField(max_digits=3, decimal_places=2, blank=True, help_text="0-999 minutes")

    notes = models.CharField(max_length=500, blank=True)

    def __unicode__(self):
        return self.customer.name + self.date_of_test

    class Meta:
        ordering = ['-date_of_work']


class PoolCharacteristics(models.Model):
    customer = models.ForeignKey(Customer)
    date_of_work = models.DateField(blank=False)
    name_of_pool = models.CharField(max_length=50, blank=True)

    gallons = models.DecimalField(max_digits=7, decimal_places=0, blank=True, help_text="0-999999 gallons")
    pump_runtime = models.DecimalField(max_digits=2, decimal_places=2, blank=True, help_text="0-24 hours")

    notes = models.CharField(max_length=500, blank=True)

    def __unicode__(self):
        return self.customer.name + self.name_of_pool
