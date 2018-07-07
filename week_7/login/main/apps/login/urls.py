from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^registration/$', views.registure),
    url(r'^login/$', views.login)
]
