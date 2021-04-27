from django import forms
from recipe.models import Recipe, Ingredient, Collection


class RecipeForm(forms.ModelForm):
    
    class Meta:
        model = Recipe
        fields = ('title', 'veg_or_other', 'image', 'cuisine', 'difficulty_level', 'instructions', 'servings', 'preparation_time', 'total_time', 'calories', )


class IngredientForm(forms.ModelForm):
    
    class Meta:
        model = Ingredient
        fields = ('name', 'quantity', 'measurement', )


class CollectionForm(forms.ModelForm):
    
    class Meta:
        model = Collection
        fields = ('name', 'recipe')