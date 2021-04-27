from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User


class Recipe(TimeStampedModel):
    title = models.CharField(max_length=512)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    Veg_CHOICES = (
        ('Veg', 'Veg'),
        ('Vegan', 'Vegan'),
        ('Non-Veg', 'Non-Veg'),
    )
    veg_or_other = models.CharField(max_length=10, choices=Veg_CHOICES)

    image = models.ImageField(upload_to='image', null=True, blank=True)
    cuisine = models.CharField(max_length=2000, null=True, blank=True)

    difficulty_choices = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    )
    difficulty_level = models.CharField(max_length=1, choices=difficulty_choices)

    instructions = models.TextField()
    servings = models.IntegerField(default=0)
    preparation_time = models.IntegerField(default=0)
    total_time = models.IntegerField(default=0)
    calories = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return '{} by {}'.format(self.title, self.author)


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    quantity = models.DecimalField(decimal_places=2, max_digits=5, default=0, blank=True)
    measurement = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Collection(models.Model):
    name = models.CharField(max_length=200)
    recipe = models.ManyToManyField(Recipe)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name