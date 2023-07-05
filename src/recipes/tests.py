from django.test import TestCase
from .models import Recipe
from .forms import DifficultySearchForm

# Create your tests here.


class RecipeModelTest(TestCase):
    def setUpTestData():
        Recipe.objects.create(name='Tea', cooking_time='3',
                              ingredients='Water, Tea Leaves')

    def test_recipe_name_length(self):
        recipe = Recipe.objects.get(id=1)
        name_max_length = recipe._meta.get_field('name').max_length
        self.assertEqual(name_max_length, 120)

    def test_recipe_name(self):
        recipe = Recipe.objects.get(id=1)
        recipe_name_label = recipe._meta.get_field('name').verbose_name
        self.assertEqual(recipe_name_label, 'name')

    def test_cooking_time(self):
        recipe = Recipe.objects.get(id=1)
        recipe_cooking_time = recipe.cooking_time
        self.assertEqual(recipe_cooking_time, 3)

    def test_ingredients_list(self):
        recipe = Recipe.objects.get(id=1)
        recipe_ingredients = recipe.ingredients
        self.assertEqual(recipe_ingredients, 'Water, Tea Leaves')

    def test_get_absolute_url(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.get_absolute_url(), '/list/1')

    def test_difficulty_calculation(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.calculate_difficulty(), 'Easy')


class RecipesSearchFormTest(TestCase):
    def test_form_renders_recipe_difficulty_input(self):
        form = DifficultySearchForm()
        self.assertIn('recipe_diff', form.as_p())

    def test_form_renders_chart_type_input(self):
        form = DifficultySearchForm()
        self.assertIn('chart_type', form.as_p())

    def test_form_valid_data(self):
        form = DifficultySearchForm(
            data={'recipe_diff': '#1', 'chart_type': '#2'})
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form = DifficultySearchForm(
            data={'recipe_diff': '', 'chart_type': ''})
        self.assertFalse(form.is_valid())
