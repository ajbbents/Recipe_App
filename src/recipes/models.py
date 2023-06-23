from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(default='this will be delicious!')
    cooking_time = models.FloatField(help_text="in minutes")
    difficulty = models.CharField(max_length=20)
    ingredients = models.TextField()
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')

    def __str__(self):
        return str(self.name)
