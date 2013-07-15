# Create your views here.
__author__ = 'robertv'
__copyright__ = "QED Testing, Inc. 2013"

from django.http import HttpResponse

from CaracalApp.forms import ItemForSaleForm, HuntItemForm

from CaracalApp.services import get_items_for_sale, add_item_for_sale, get_item_details
from CaracalApp.services import get_sellers, get_contact_info
from CaracalApp.services import get_hunt_list, add_hunt_entry

from CaracalApp.message_strings import section_show_items, section_show_details
from CaracalApp.message_strings import section_sell_item, section_add_hunt
from Common.message_strings import  invalid_not_logged_in

from Common.view_helpers import render_template


def home(request):
    seller_list = get_sellers(None)
    action_template = "Caracal/General/HomePage.htm"
    return render_action_template(request, locals())

def about(request):
    debug_text = " Language:" + request.LANGUAGE_CODE + ":"
    action_template = "Caracal/General/About.htm"
    return render_action_template(request, locals())



def items_for_sale(request):
    if "filter" in request.GET:
        items_for_sale = get_items_for_sale(request.GET['filter'])
    else:
        items_for_sale = get_items_for_sale(None)

    current_section = section_show_items
    action_template = "Caracal/ForSale_actions/ForSaleItems.htm"
    return render_action_template(request, locals())

def item_details(request, item_id):
    item = get_item_details(item_id)
    if item != None:
        email, subject, body = get_contact_info(item)

        current_section = section_show_details
        action_template = "Caracal/ForSale_actions/ItemDetails.htm"
        return render_action_template(request, locals())
    else:
        return render_template(request, "ItemNotFound.html", locals())

def sell_an_item(request):
    if request.user.is_anonymous():
        return HttpResponse(invalid_not_logged_in)

    if request.method == 'POST':
        form=ItemForSaleForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            if request.FILES.has_key('file'):
                fileSize = request.FILES['file'].size
            else:
                fileSize = 0
            email_count = add_item_for_sale(cd['title'], cd['description'], cd['price'], request.user)
            created=True
            form = ItemForSaleForm()
    else:
        form = ItemForSaleForm()

    current_section = section_sell_item
    action_template = "Caracal/ForSale_actions/AddForSaleItem.htm"
    return render_action_template(request, locals())



def hunt_list(request):
    if "filter" in request.GET:
        notice_requests = get_hunt_list(request.GET['filter'])
    else:
        notice_requests = get_hunt_list(None)
    form = HuntItemForm()

    if request.method == 'POST':
        form=HuntItemForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            add_hunt_entry(cd['title'], cd['search_text'], cd['email'])
            form = HuntItemForm()

    current_section = section_add_hunt
    action_template = "Caracal/HuntList_actions/HuntList.htm"
    return render_action_template(request, locals())


def render_action_template(request, p_locals):
    assert p_locals["request"].user != None
    return render_template(request, 'Caracal/CaracalHomePage.html', p_locals)