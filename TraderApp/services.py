__author__ = 'robertv'

import datetime
from models import HuntEntry, ItemForSale, Seller
from listing_processor import add_a_listing

#
# CRUD for ItemForSale objects
#
def get_items_for_sale(filter):
    if not filter:
        return ItemForSale.objects.all()
    else:
        return ItemForSale.objects.filter(description__icontains=filter)

def get_item_details(item_id):
    return ItemForSale.objects.get(id=item_id)

def add_item_for_sale(title, description, cost, seller_id):
    count = add_a_listing(title, description, cost, seller_id)
    return count


#
# CRUD for HuntEntry
#
def get_hunt_list(filter):
    if not filter:
        return HuntEntry.objects.all()
    else:
        return HuntEntry.objects.filter(search_text__icontains=filter)

def add_hunt_entry(title, search_text, email):
    item = HuntEntry(title=title,
                       search_text=search_text,
                       email = email,
                       create_date = datetime.datetime.now())
    item.save()


#
# CRUD for Seller
#
def get_sellers(filter):
    if not filter:
        return Seller.objects.filter(active = True)
    else:
        return Seller.objects.filter(active = True,name__icontains=filter)
