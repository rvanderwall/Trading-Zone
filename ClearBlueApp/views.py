# views.py
__author__ = 'robertv'
__copyright__ = "QED Testing, Inc. 2013"

import django.http

from Common.view_helpers import render_template
from Common.message_strings import  invalid_not_logged_in

from message_strings import section_add_test, section_show_tests
from forms import PoolChemicalTest
from services import create_pool_test, get_pool_tests


def about(request):
    debug_text = " Language:" + request.LANGUAGE_CODE + ":"
    action_template = "ClearBlue/General/About.htm"
    return render_action_template(request, locals())

def pool_help(request):
    action_template = "ClearBlue/PoolHelpMain.htm"
    return render_action_template(request, locals())

def pool_maint(request):
    action_template = "ClearBlue/PoolHelpMain.htm"
    return render_action_template(request, locals())

def chem_test(request):
#    if request.user.is_anonymous():
#        return django.http.HttpResponse(invalid_not_logged_in)

    if request.method == 'POST':
        form=PoolChemicalTest(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            create_pool_test(cd['title'], cd['description'], cd['price'], request.user)
            created=True
            form = PoolChemicalTest()
    else:
        form = PoolChemicalTest()

    current_section = section_add_test
    pool_test_results = get_pool_tests()
    action_template = "ClearBlue/AddChemicalTest.htm"
    return render_action_template(request, locals())


def chem_test_results(request):
    if "filter" in request.GET:
        pool_test_results = get_pool_tests(request.GET['filter'])
    else:
        pool_test_results = get_pool_tests(None)

    current_section = section_show_tests
    action_template = "ClearBlue/ShowPoolTests.htm"
    return render_action_template(request, locals())


def pool_help(request):
    action_template = "ClearBlue/PoolHelpMain.htm"
    return render_action_template(request, locals())

def render_action_template(request, p_locals):
    return render_template(request, 'ClearBlue/ClearBlueHomePage.html', p_locals)