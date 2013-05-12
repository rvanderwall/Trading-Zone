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
    item = ItemForSale.objects.get(id=item_id)
    return item

def get_contact_info(item):
    email = item.seller.email
    name = item.seller.name
    subject = "Hello, " + name + ". I'm interested in the item you have for sale."
    body = subject + "\nPlease let me know if it's still available.\nThanks"
    return email, subject, body

def add_item_for_sale(title, description, cost, user):
    seller = get_seller_for_user(user)
    count = add_a_listing(title, description, cost, seller)
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

def get_seller_for_user(user):
    return Seller.objects.get(user=user)

def create_seller(user):
    s1 = Seller(user=user,
            name=user.username,
            address="No Address provided",
            city="No City provided",
            state="No State provided",
            email=user.email,
            creation_date=datetime.datetime.now(),
            active=True)
    s1.save()
