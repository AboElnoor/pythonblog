"""pythonblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^$',index),
	url(r'^latest_5$',latest_5),
	url(r'^single/(?P<post_id>[0-9]+)/$',single),
    url(r'^register$',register),
    url(r'^login$',login),
    url(r'^signin$',signin),
    url(r'^loggedin$',loggedin),
    url(r'^invalid$',invalid),
    url(r'^logout_view$',logout_view),
    url(r'^(?P<user_id>[0-9]+)/add_article$', add_article),
    url(r'^(?P<art_id>[0-9]+)/edit_article$', edit_article),
    url(r'^(?P<comm_id>[0-9]+)/add_comment$', add_comment),
    url(r'^single/(?P<post_id>[0-9]+)/(?P<comm_id>[0-9]+)/edit_comment$', edit_comment),
    url(r'^passreset/$',auth_views.password_reset,name='password_reset'),
    url(r'^passresetdone/$',auth_views.password_reset_done,name='password_reset_done'),
    url(r'^passresetconfirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',auth_views.password_reset_confirm,name='registration/password_reset_email.html'),
    url(r'^passresetcomplete/$',auth_views.password_reset_complete,name='password_reset_complete'),
]
