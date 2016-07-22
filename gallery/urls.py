from django.conf.urls import include, url
from django.contrib import admin

from .views import (
album_detail,
contact,
home,
post_detail,
post_list,
thanks,
)

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^contact/thank-you/$', thanks, name='thanks'),
    url(r'^albums/(?P<slug>[\w-]+)/$', album_detail, name = 'album_detail'),
    url(r'^post/$', post_list, name="post_list"),
    url(r'^post/(?P<slug>[\w-]+)/$', post_detail, name="post_detail"),

    ]
