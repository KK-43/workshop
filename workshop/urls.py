from django.conf.urls import patterns, include, url

from django.contrib import admin
from registration.views import Home
from registration import urls as register

urlpatterns = patterns('',
   # Examples:
   # url(r'^$', 'prasad.views.home', name='home'),
   # url(r'^blog/', include('blog.urls')),
   url(r'^admin/', include(admin.site.urls)),
   url(r'^register/', include(register)),
   url(r'^$', Home.as_view(), name='home')
)