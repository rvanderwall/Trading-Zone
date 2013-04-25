from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from SimpleApp.views import hello, current_datetime, hours_ahead
from TraderApp import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'RobertsSite.views.home', name='home'),
    # url(r'^RobertsSite/', include('RobertsSite.foo.urls')),
    (r'^hello/$', hello),
    (r'^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    #
    (r'^home/$', views.home),
    (r'^forSaleItems/$', views.items_for_sale),
    (r'^itemDetails/(\d{1,2})/$', views.itemDetails),
    (r'^sellAnItem/$', views.requires_login(views.sellAnItem)),
    (r'^searchNotifications/$', views.requires_login(views.hunt_list)),
    (r'^seed/$', views.requires_login(views.seed)),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()