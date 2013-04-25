# Create your views here.
import datetime
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

from SeedData import SeedSellers
from services import get_items_for_sale, add_item_for_sale, get_item_details
from services import get_sellers
from services import get_hunt_list, add_hunt_entry
from forms import ItemForSaleForm, HuntItemForm

def home(request):
    current_date = datetime.datetime.now()
    current_section = "Home"
    action_template = "Sellers/SellersTemplate.html"
    seller_list = get_sellers(None)
    return render_to_response('TraderHomeTemplate.html', locals())

def requires_login(view):
    authorized = True
    def new_view(request, *args, **kwargs):
        if not authorized:
            return HttpResponseRedirect('/login/')
        return view(request, *args, **kwargs)
    return new_view


def seed(request):
    SeedSellers()
    return render_to_response('SeedTemplate.html', locals())



def items_for_sale(request):
    if "filter" in request.GET:
        items_for_sale = get_items_for_sale(request.GET['filter'])
    else:
        items_for_sale = get_items_for_sale(None)

    current_section = "Show Items For Sale"
    action_template = "ForSale/ForSaleItemsTemplate.html"
    current_date = datetime.datetime.now()
    c = {}
    c.update(csrf(request))
    c.update(locals())
    return render_to_response('TraderHomeTemplate.html', c)

def itemDetails(request, item_id):
    item = get_item_details(item_id)

    current_section = "Show Item details"
    action_template = "ForSale/ItemDetailsTemplate.html"
    current_date = datetime.datetime.now()
    c = {}
    c.update(csrf(request))
    c.update(locals())
    return render_to_response('TraderHomeTemplate.html', c)

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
    action_template = "ForSale/AddForSaleItemTemplate.html"
    current_date = datetime.datetime.now()
    c = {}
    c.update(csrf(request))
    c.update(locals())
    return render_to_response('TraderHomeTemplate.html', c)



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
    action_template = "HuntList/HuntListTemplate.html"
    current_date = datetime.datetime.now()
    c = {}
    c.update(csrf(request))
    c.update(locals())
    return render_to_response('TraderHomeTemplate.html', c)
