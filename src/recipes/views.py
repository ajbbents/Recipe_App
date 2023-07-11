from django.shortcuts import render  # default import
from django.views.generic import ListView, DetailView  # to display lists, details
from .models import Recipe  # to access Recipe model
# to protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import DifficultySearchForm, CreateRecipeForm
import pandas as pd
from .utils import get_recipename_from_id, get_chart


class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/recipes_list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'


def recipes_home(request):
    return render(request, 'recipes/recipes_home.html')


def about_view(request):
    return render(request, 'recipes/about.html')


# define function-based view: records
def records(request):
    # create instance of DifficultySearchForm
    form = DifficultySearchForm(request.POST or None)
    recipe_df = None  # initialize dataframe to none
    recipe_diff = None
    chart = None
    qs = None

    # check if button is clicked
    if request.method == 'POST':
        # read recipe_diff and chart_type
        recipe_diff = request.POST.get('recipe_diff')
        chart_type = request.POST.get('chart_type')

        if recipe_diff == '#1':
            recipe_diff = 'Easy'
        if recipe_diff == '#2':
            recipe_diff = 'Medium'
        if recipe_diff == '#3':
            recipe_diff = 'Intermediate'
        if recipe_diff == '#4':
            recipe_diff = 'Hard'

        qs = Recipe.objects.all()
        id_searched = []
        for obj in qs:
            diff = obj.calculate_difficulty()
            if diff == recipe_diff:
                id_searched.append(obj.id)

        qs = qs.filter(id__in=id_searched)

        if qs:  # if data found
            # convert the queryset values to pandas df
            recipe_df = pd.DataFrame(qs.values())
            chart = get_chart(chart_type, recipe_df,
                              labels=recipe_df['name'].values)

            recipe_df = recipe_df.to_html()

    # pack data to be sent to template in context dictionary
    context = {
        'form': form,
        'recipe_df': recipe_df,
        'chart': chart,
        'qs': qs,
    }

    return render(request, 'recipes/search.html', context)

# login required


def create_view(request):
    create_form = CreateRecipeForm(request.POST or None, request.FILES)
    name = None
    cooking_time = None
    ingredients = None

    if request.method == 'POST':
        try:
            recipe = Recipe.objects.create(
                name=request.POST.get('name'),
                cooking_time=request.POST.get('cooking_time'),
                ingredients=request.POST.get('ingredients'),
                description=request.POST.get('description'),
            )
            recipe.save()

        except:
            print('Well, shoot. Try again.')

    context = {
        'create_form': create_form,
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients,
    }

    return render(request, 'recipes/create.html', context)
