from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^record$', views.record),
    url(r'^signin$', views.signin),
    url(r'^dashboard$', views.dashboard),
    url(r'^logout$', views.logout),
    url(r'^wall/(?P<id>\d+)$', views.wall),
    url(r'^wall/create_post/(?P<id>\d+)$', views.wall),
    url(r'^create_post/(?P<id>\d+)$', views.create_post),
]