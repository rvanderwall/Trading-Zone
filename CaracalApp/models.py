# models.py
__author__ = 'robertv'
__copyright__ = "QED Testing, Inc. 2013"

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from message_strings import help_name, help_address

class Seller(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=30, help_text= help_name)
    address = models.CharField(max_length=100, help_text= help_address)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50, blank=True)
    active = models.BooleanField()
    website = models.URLField(blank=True)
    email = models.EmailField()
    creation_date = models.DateField(blank=True, null=True)
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('seller')
        verbose_name_plural = _('sellers')
        ordering = ['name']


class ItemForSale(models.Model):
    seller = models.ForeignKey(Seller)
    title = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=4000, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True )
    listing_date = models.DateField(blank=False)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-listing_date']


class HuntEntry(models.Model):
    title = models.CharField(max_length=50, blank=False)
    search_text = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
    create_date = models.DateField(blank=False)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-create_date']


class Recommendation(models.Model):
    who_recommended = models.CharField(max_length=30)
    recommendation = models.CharField(max_length=100)
    who_was_recommended = models.ForeignKey(Seller)
    date_of_recommendation = models.DateField()

    def __unicode__(self):
        return self.who_recommended + " recommended " + self.who_was_recommended
