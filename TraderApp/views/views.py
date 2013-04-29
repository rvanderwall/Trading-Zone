# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

from TraderApp.SeedData import SeedSellers
from TraderApp.services import get_items_for_sale, add_item_for_sale, get_item_details
from TraderApp.services import get_sellers
from TraderApp.services import get_hunt_list, add_hunt_entry
from TraderApp.forms import ItemForSaleForm, HuntItemForm
from TraderApp.views.view_helpers import render_action_template


def home(request):
    seller_list = get_sellers(None)

    current_section = "Home"
    action_template = "Sellers_actions/Sellers.htm"
    return render_action_template(request, locals())


def seed(request):
    SeedSellers()
    return render_to_response('SeedPage.html', locals())



def items_for_sale(request):
    if "filter" in request.GET:
        items_for_sale = get_items_for_sale(request.GET['filter'])
    else:
        items_for_sale = get_items_for_sale(None)

    current_section = "Show Items For Sale"
    action_template = "ForSale_actions/ForSaleItems.htm"
    return render_action_template(request, locals())

def itemDetails(request, item_id):
    item = get_item_details(item_id)

    current_section = "Show Item details"
    action_template = "ForSale_actions/ItemDetails.htm"
    return render_action_template(request, locals())

def sellAnItem(request):
    if request.user.is_anonymous():
        return HttpResponse("You are not logged in")

    if request.method == 'POST':
        form=ItemForSaleForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            add_item_for_sale(cd['title'], cd['description'], cd['price'], 2)
            created=True
            form = ItemForSaleForm()
    else:
        form = ItemForSaleForm()

    current_section = "Sell an Item"
    action_template = "ForSale_actions/AddForSaleItem.htm"
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

    current_section = "Add a search request"
    action_template = "HuntList_actions/HuntList.htm"
    return render_action_template(request, locals())

