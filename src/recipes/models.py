from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=120)
    cooking_time = models.FloatField(help_text="in minutes")
    difficulty = models.CharField(max_length=20)
    ingredients = models.TextField()

    def __str__(self):
        return str(self.name)
