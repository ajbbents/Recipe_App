from django.shortcuts import render  # default import
from django.views.generic import ListView, DetailView  # to display lists, details
from .models import Recipe  # to access Recipe model
# to protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/recipes_list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'


def recipes_home(request):
    return render(request, 'recipes/recipes_home.html')
