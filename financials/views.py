# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create Financial Here

class FinancialCreateView(LoginRequiredMixin, CreateView):
    model = models.Financial
    template_name = 'Financial/Financial_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = ['Financial_Status','Financial_Date']

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Financial Details Here


class FinancialDetailView(LoginRequiredMixin, DetailView):
    model = models.Financial
    template_name = 'Financial/Financial_detail.html'
    login_url = 'login'

# Financial ListView Here


class FinancialListView(ListView):
    model = models.Financial
    template_name = 'Financial/Financial_list.html'
    login_url = 'login'

# Financial Update Here


class FinancialUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Financial

    # Decide fields for editing Here

    fields = ['Financial_Status','Financial_Date']
    template_name = 'Financial/Financial_update.html'
    login_url = 'login'

# Financial Delete here


class FinancialDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Financial
    template_name = 'Financial/Financial_delete.html'
    success_url = reverse_lazy('Financial_list')
    login_url = 'login'



from django.shortcuts import render

# Create your views here.
