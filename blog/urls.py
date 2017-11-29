from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.contrib.auth.views import login, logout
from blog import views as myapp_views
from django.contrib.auth import views
from django.conf import settings


urlpatterns = [
    url(r'^home/$', myapp_views.home, name='home'),
    url(r'^post/(?P<pk>[0-9]+)/$', myapp_views.post_detail, name='post_detail'),
    url(r'^post/new/$', myapp_views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', myapp_views.post_edit, name='post_edit'),
    url(r'^accounts/register/$', myapp_views.register, name='register'),
    url(r'^accounts/register/complete/$', myapp_views.registration_complete,name='registration_complete'),
    url(r'^accounts/login$', views.login, name='login'),
    #url(r'^accounts/logout/$', views.logout, name='logout'),
    url(r'^accounts/logout/$', views.logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    #url(r'^accounts/logout/$', views.logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    #url(r'^accounts/loggedin/$', myapp_views.loggedin, name='loggedin'),
]
