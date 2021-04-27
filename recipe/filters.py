import django_filters 
from .models import Recipe
 

class RecipeFilter(django_filters.FilterSet):

    class Meta:
        model = Recipe
        fields = ['author', 'cuisine', 'difficulty_level', 'veg_or_other']

   

  