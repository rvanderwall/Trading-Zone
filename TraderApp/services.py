__author__ = 'robertv'

import datetime
from models import HuntEntry, ItemForSale, Seller
from listing_processor import get_emails_to_notify

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
    seller = Seller.objects.get(id=seller_id)
    item = ItemForSale(title=title,
                       description=description,
                       price = cost,
                       listing_date = datetime.datetime.now(),
                       seller = seller)
    item.save()
    list_of_emails = get_emails_to_notify(item.description)
    for email in list_of_emails:
        print "Saved item " + item.title + " notified " + email

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
