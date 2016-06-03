
from django.conf.urls import patterns, include,url
from django.contrib import admin
from registration.views import Home
from registration.views import UserRegistrationView
urlpatterns = patterns('',
   # Examples:
   # url(r'^$', 'prasad.views.home', name='home'),
   # url(r'^blog/', include('blog.urls')),
   url(r'^registration/', UserRegistrationView.as_view(), name='register_user')
)