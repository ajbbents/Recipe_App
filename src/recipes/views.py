from django.shortcuts import render  # default import
from django.views.generic import ListView, DetailView  # to display lists, details
from .models import Recipe  # to access Recipe model

# Create your views here.


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/main.html'


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'


def recipes_home(request):
    return render(request, 'recipes/recipes_home.html')
