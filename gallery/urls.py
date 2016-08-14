from django.conf.urls import  url

from .views import (
album_detail,
contact,
home,
thanks,
)

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^contact/$', contact, name='contact'),
    url(r'^contact/thank-you/$', thanks, name='thanks'),
    url(r'^albums/(?P<slug>[\w-]+)/$', album_detail, name='album_detail'),

    ]
