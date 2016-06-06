from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.conf.urls import patterns, include,url
from django.contrib import admin
from registration.views import Home
from registration.views import UserRegistrationView
from workshop.views import anonymous_required
import registration.views as views
from registration.views import *


urlpatterns = patterns('',
   # Examples:
   # url(r'^$', 'prasad.views.home', name='home'),
   # url(r'^blog/', include('blog.urls')),
   url(r'^registration/', UserRegistrationView.as_view(), name='register_user'),
   url(r'^user/$', UserRegistrationView.as_view(), name='register_user'),
   url(r'^user/success/', TemplateView.as_view(template_name='success.html'),name='user_registration_success'),
                       url(r'^user/login/$',
                           anonymous_required(auth_views.login),
                           {'template_name': 'login.html'},
                           name='login'),

                       url(r'^user/logout/$',
                           auth_views.logout,
                           {'template_name': 'logout.html'},
                           name='logout'),
    url(r'^chocolate/add/',AddChocolateView.as_view(),name="add_chocolate")
   )