from django.shortcuts import render
from recipe.models import Recipe


def recipe_list(request):
    recipe_list = Recipe.objects.all()

    context = {
        "recipe_list": recipe_list,
    }
    return render(request, 'recipe/recipe_list.html', context=context)

