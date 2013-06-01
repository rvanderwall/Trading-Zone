from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from SimpleApp.views import hello, current_datetime, hours_ahead

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from CaracalApp.views import views, registration_views, view_helpers


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TradingZoneSite.views.home', name='home'),
    # url(r'^TradingZoneSite/', include('TradingZoneSite.foo.urls')),
    (r'^hello/$', hello),
    (r'^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    )

urlpatterns += patterns('',
    (r'^tz/$', views.home),
    (r'^home/$', views.home),
    (r'^about/$', views.about),
    (r'^register/$', registration_views.register),
    (r'^login/$', registration_views.login),
    (r'^logout/$', registration_views.logout),
    (r'^forSaleItems/$', views.items_for_sale),
    (r'^itemDetails/(\d{1,2})/$', views.itemDetails),
    (r'^sellAnItem/$', view_helpers.requires_login(views.sellAnItem)),
    (r'^searchNotifications/$', view_helpers.requires_login(views.hunt_list)),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()