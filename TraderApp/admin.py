__author__ = 'robertv'

from django.contrib import admin
from TraderApp.models import Seller, Recommendation, ItemForSale, HuntEntry

class SellerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'state')
    list_filter = ('active',)

admin.site.register(Seller, SellerAdmin)
admin.site.register(Recommendation)
admin.site.register(ItemForSale)
admin.site.register(HuntEntry)


