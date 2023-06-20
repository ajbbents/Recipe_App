from django.test import TestCase
from .models import Recipe

# Create your tests here.


class RecipeModelTest(TestCase):
    def setUpTestData():
        Recipe.objects.create(name='Tea', cooking_time='3',
                              difficulty='Easy', ingredients='Water, Tea Leaves')

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

    def test_difficulty_length(self):
        recipe = Recipe.objects.get(id=1)
        max_difficulty_length = recipe._meta.get_field('difficulty').max_length
        self.assertEqual(max_difficulty_length, 20)

    def test_ingredients_list(self):
        recipe = Recipe.objects.get(id=1)
        recipe_ingredients = recipe.ingredients
        self.assertEqual(recipe_ingredients, 'Water, Tea Leaves')