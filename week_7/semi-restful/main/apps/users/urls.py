from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^user/create/$', views.create),
    url(r'^user/create/add/$', views.add),
    url(r'^show/(?P<user_id>\d+)$', views.show),
    url(r'^show/(?P<user_id>\d+)/edit$', views.edit),
    url(r'^show/(?P<user_id>\d+)/show/$', views.show),
    url(r'^show/(?P<user_id>\d+)/change/$', views.change),
    url(r'^(?P<user_id>\d+)/edit$', views.edit),
    url(r'^(?P<user_id>\d+)/change/$', views.change),
    url(r'^(?P<user_id>\d+)/delete/$', views.delete),
    url(r'^show/(?P<user_id>\d+)/delete/$', views.delete),
]