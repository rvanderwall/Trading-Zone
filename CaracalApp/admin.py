# admin.py
__author__ = 'robertv'
__copyright__ = "QED Testing, Inc. 2013"

from django.contrib import admin
from CaracalApp.models import Seller, Recommendation, ItemForSale, HuntEntry

# set up model for use in 'admin' pages.  Each model that will be managed needs
# to be registered.

class SellerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'state')
    list_filter = ('active',)

admin.site.register(Seller, SellerAdmin)
admin.site.register(Recommendation)
admin.site.register(ItemForSale)
admin.site.register(HuntEntry)


