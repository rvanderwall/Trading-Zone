# Create your views here.

from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404
import datetime
from models import  Book

def latest_books(request):
    book_list = Book.objects.order_by('-pub_date')[:10]
    return render_to_response('latest_books.html', {'book_list':book_list})

def hello(request):
    return HttpResponse("Hello World")

# Get a template and render it using a context.
def current_datetime0(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

# use render_to_response to template and render in one call
def current_datetime1(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date':now})

# use locals() so we don't need to build a map.
# NOTE:  ALL locals are passed, so use with some care.
def current_datetime(request):
    current_date = datetime.datetime.now()
    current_section = "Current Date"
    return render_to_response('current_datetime.html', locals())

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>It is now %s in the TZ %s.</body></html>" % (dt, offset)
    return HttpResponse(html)
