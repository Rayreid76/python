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
    url(r'^wall$', views.wall),
    url(r'^create_post$', views.create_post),
    url(r'^delete_post/(?P<id>\d+)$', views.delete_post),
    url(r'^make_comment/(?P<id>\d+)$', views.make_comment),
    url(r'^profile$', views.profile),
    url(r'^edit_user_name$', views.edit_user_name),
    url(r'^edit_user_password$', views.edit_user_password),
    url(r'^delete_user/(?P<id>\d+)$', views.delete_user),
    url(r'^adminupdate/(?P<id>\d+)$', views.adminupdate),
    url(r'^edit_admin_name/(?P<id>\d+)$', views.edit_admin_name),
    url(r'^edit_admin_password/(?P<id>\d+)$', views.edit_admin_password),
    url(r'^add_user$', views.add_user)
]