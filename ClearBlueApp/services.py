# services.py
__author__ = 'robertv'
__copyright__ = "QED Testing, Inc. 2013"

import datetime
from models import ChemicalPoolTest

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


def create_pool_test(title, description, cost, user):
    s1 = ChemicalPoolTest(customer=user,
            ph=0.0,
            acid_demand=0.0,
            chlorine_level=0.0,
            bromine_level=0.0,
            alkalinity=0.0,
            hardness=0.0,
            notes="notes",
            date_of_test=datetime.datetime.now())
    s1.save()

