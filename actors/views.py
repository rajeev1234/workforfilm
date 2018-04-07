# from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # for autherising users

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models

from django.urls import reverse_lazy


# Create your views here.

# Create Actor Here

class ActorCreateView(LoginRequiredMixin, CreateView):
    model = models.Actor
    template_name = 'actors/actors_new.html'
    login_url = 'login'

    # Decide fields for taking input Here

    fields = [
'Actor_Body_Type',

'Actor_Ethnicity',
'Actor_Eye_Color',
'Actor_Favorite_Acting_Styles',
'Actor_Height',
'Actor_SceneComfort',
'Actor_Skin_Color',
'Actor_Smoker',
'Actor_Weight',
        'Actor_Description',
             # 'Actors_profileproject',
             #  'Actors_Portfolio',
             #
             #  'Actor_Financials',

              ]

    # Set fields from current data or automated data

    def form_valid(self, form):
        form.instance.user= self.request.user
        return super().form_valid(form)

# Actor Details Here


class ActorDetailView(LoginRequiredMixin, DetailView):
    model = models.Actor
    template_name = 'actors/actors_detail.html'
    login_url = 'login'

# Actor ListView Here


class ActorListView(ListView):
    model = models.Actor
    template_name = 'actors/actors_list.html'
    login_url = 'login'

# Actor Update Here


class ActorUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Actor

    # Decide fields for editing Here

    fields = [
'Actor_Body_Type',

'Actor_Ethnicity',
'Actor_Eye_Color',
'Actor_Favorite_Acting_Styles',
'Actor_Height',
'Actor_SceneComfort',
'Actor_Skin_Color',
'Actor_Smoker',
'Actor_Weight',
        'Actor_Description',

              # 'Actors_profileproject',
              # 'Actors_Portfolio',
              # 'Actor_Financials'
              ]

    template_name = 'actors/actors_update.html'
    login_url = 'login'

# Actor Delete here


class ActorDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Actor
    template_name = 'actors/actors_delete.html'
    success_url = reverse_lazy('actor_list')
    login_url = 'login'



