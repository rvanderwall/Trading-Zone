# services.py
__author__ = 'robertv'
__copyright__ = "QED Testing, Inc. 2013"

import datetime
from models import ChemicalPoolTest, Customer
from Common.message_strings import default_state, default_city, default_address

#
# CRUD for ChemicalPoolTest objects
#
def get_pool_tests(filter):
    if not filter:
        return ChemicalPoolTest.objects.all()
    else:
        return ChemicalPoolTest.objects.filter(description__icontains=filter)

def get_single_pool_test(pool_test_id):
    item = ChemicalPoolTest.objects.get(id=pool_test_id)
    return item


def create_pool_test(ph, chlorine, user):
    s1 = ChemicalPoolTest(customer=get_customer_for_user(user),
            ph=ph,
            acid_demand=0.0,
            chlorine_level=chlorine,
            bromine_level=0.0,
            alkalinity=0.0,
            hardness=0.0,
            notes="notes",
            date_of_test=datetime.datetime.now())
    s1.save()


#
# CRUD for Customer
#
def get_customer(filter):
    if not filter:
        return Customer.objects.filter(active = True)
    else:
        return Customer.objects.filter(active = True, name__icontains=filter)

def get_customer_for_user(user):
    return Customer.objects.get(user=user)

def create_customer(user):
    s1 = Customer(user=user,
            name=user.username,
            address= default_address,
            city= default_city,
            state= default_state,
            email=user.email,
            creation_date=datetime.datetime.now(),
            active=True)
    s1.save()

