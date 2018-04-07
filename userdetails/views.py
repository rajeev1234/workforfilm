# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create userdetails Here

class UserDetailsCreateView(LoginRequiredMixin, CreateView):
    model = models.UserDetails
    template_name = 'userdetails/userdetails_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = [
        'UserDetail_First_Name',
        'UserDetail_Last_Name',
        'UserDetails_Phone',
        'UserDetail_Date_Of_Birth',
        'UserDetail_Gender',
        'UserDetail_Street_Address',
        'UserDetail_City',
        'UserDetail_State',
        'UserDetail_Country',
        'UserDetail_Pin_Code',
        'UserDetail_Official_ID',
        'UserDetail_Profile_Picture',
        'UserDetail_User_Description',
        'UserDetail_Completed',
    ]

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.UserDetails_First_Name = self.request.user
        return super().form_valid(form)


# userdetails Details Here


class UserDetailsDetailView(LoginRequiredMixin, DetailView):
    model = models.UserDetails
    template_name = 'userdetails/userdetails_detail.html'
    login_url = 'login'


# userdetails ListView Here


class UserDetailsListView(ListView):
    model = models.UserDetails
    template_name = 'userdetails/userdetails_list.html'
    login_url = 'login'


# userdetails Update Here


class UserDetailsUpdateView(LoginRequiredMixin, UpdateView):
    model = models.UserDetails

    # Decide fields for editing Here

    fields = [
        'UserDetail_First_Name',
        'UserDetail_Last_Name',
        'UserDetails_Phone',
        'UserDetail_Date_Of_Birth',
        'UserDetail_Gender',
        'UserDetail_Street_Address',
        'UserDetail_City',
        'UserDetail_State',
        'UserDetail_Country',
        'UserDetail_Pin_Code',
        'UserDetail_Official_ID',
        'UserDetail_Profile_Picture',
        'UserDetail_User_Description',
        'UserDetail_Completed',
    ]
    template_name = 'userdetails/userdetails_update.html'
    login_url = 'login'


# userdetails Delete here


class UserDetailsDeleteView(LoginRequiredMixin, DeleteView):
    model = models.UserDetails
    template_name = 'userdetails/userdetails_delete.html'
    success_url = reverse_lazy('userdetails_list')
    login_url = 'login'



