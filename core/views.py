from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse

from .models import Listing


class HomeView(ListView):
    template_name = 'home.html'
    queryset = Listing.objects.filter(flagged=False)
    context_object_name = 'listings'
    paginate_by = 30


class CreateListing(LoginRequiredMixin, CreateView):
    model = Listing
    fields = ['title', 'content', 'category', 'expiry_date', 'location']
    template_name = 'add_listing.html'

    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ListingView(DetailView):
    template_name = 'listing.html'
    model = Listing

    def get_object(self):
        obj = super(ListingView, self).get_object()
        if obj.flagged:
            raise Http404()
        return obj