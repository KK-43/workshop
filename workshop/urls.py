from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from registration.views import UserRegistrationView
from workshop.views import anonymous_required
import registration.views as views

from django.contrib import admin
from registration.views import Home
from registration import urls as register

urlpatterns = patterns('',
   # Examples:
   # url(r'^$', 'prasad.views.home', name='home'),
   # url(r'^blog/', include('blog.urls')),
   url(r'^admin/', include(admin.site.urls)),
   url(r'^register/', include(register)),
   url(r'^$', Home.as_view(), name='home'),
   url(r'^user/login/$',
       anonymous_required(auth_views.login),
       {'template_name': 'login.html'},
       name='login'),

   url(r'^user/logout/$',
       auth_views.logout,
      {'template_name': 'logout.html'},
      name='logout'),
)