# SeedData.py
__author__ = 'robertv'
__copyright__ = "QED Testing, Inc. 2013"

from models import Seller, ItemForSale
from django.contrib.auth.models import User

import datetime


def SeedSellers():
    for seller_name in ['George', 'Paul', 'Ringo', 'John']:
        s1 = Seller(name=seller_name,
                    address="Abby Road",
                    city="Soho",
                    state="London",
                    email=seller_name + "@Beatles.com",
                    active=True)
        s1.save()

        for item_name in ['bird', 'house', 'chainsaw', 'motorcycle']:
            listing = ItemForSale(
                seller=s1,
                title=item_name + " for sale",
                description="great " + item_name + " for sale, like new.",
                price=50.00,
                listing_date=datetime.datetime.now()
            )
            listing.save()

    user = User.objects.create_user(username='john@beatles.com', password='password')
    user.is_staff = True
    user.save()