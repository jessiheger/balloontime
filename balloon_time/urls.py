from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.party_list, name='party_list'),
    url(r'(?P<pk>\d+)/$', views.party_detail, name='party_detail'),
    url(r'^post_party/$', views.PartyCreate.as_view(), name="post_party"),
    url(r'(?P<pk>[0-9]+)$', views.PartyUpdate.as_view(), name='party_update'),
    url(r'(?P<pk>[0-9]+)/delete/$', views.PartyDelete.as_view(), name='party_delete'),
    # url(r'(?P<pk>\d+)/post_clown/$', views.ClownCreate.as_view(), name="post_clown"),
    url(r'^post_clown/$', views.ClownCreate.as_view(), name="post_clown"),
    url(r'(?P<pk>\d+)/$', views.clown_detail, name='clown_detail'),

]