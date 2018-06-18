from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^run_farm/$', views.run_farm),
    url(r'^run_cave/$', views.run_cave),
    url(r'^run_house/$', views.run_house),
    url(r'^run_casino/$', views.run_casino),
]
