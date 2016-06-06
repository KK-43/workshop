from django.shortcuts import render
from django.views.generic import TemplateView
from registration.forms import *
from registration.models import *
from braces.views import LoginRequiredMixin, AnonymousRequiredMixin
from django.views.generic.edit import FormView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic import ListView
from django.http import Http404
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from django.core.mail import EmailMessage

import uuid
from string import Template
from django.views.decorators.csrf import csrf_exempt

class Home(ListView):
      template_name="index.html"

      def get_queryset(self):
          return Chocolate.objects.all()

class UserRegistrationView(AnonymousRequiredMixin, FormView):

     template_name = "register_user.html"
     authenticated_redirect_url = reverse_lazy(u"home")
     success_url = reverse_lazy(u"home")
     form_class = UserRegistrationForm
     success_url = '/register/user/success/'

     def form_valid(self, form):
        form.save()
        return FormView.form_valid(self, form)


class AddChocolateView(FormView):
    template_name="add_chocolate.html"
    form_class=ChocolateAddForm
    success_url='register/user/success'

    def form_valid(self, form):
        form.save()
        return FormView.form_valid(self, form)