from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse

from .models import Account
from .forms import RegistrationForm


class RegistrationView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegistrationForm

    def get_context_data(self, *args, **kwargs):
        context = super(RegistrationView, self).get_context_data(*args, **kwargs)
        context['next'] = self.request.GET.get('next')
        return context

    def get_success_url(self):
        next_url = self.request.POST.get('next')
        success_url = reverse('login')
        if next_url:
            success_url += '?next={}'.format(next_url)

        return success_url


class ProfileView(UpdateView):
    model = Account
    fields = ['name', 'phone', 'date_of_birth', 'picture']
    template_name = 'registration/profile.html'

    def get_success_url(self):
        return reverse('index')

    def get_object(self):
        return self.request.user