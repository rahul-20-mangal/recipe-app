from django.shortcuts import render, get_object_or_404
from recipe.models import Recipe
from recipe.filters import RecipeFilter

def recipe_list(request):
    recipe_list = Recipe.objects.all().order_by('-created','-modified','calories')
    recipe_filter = RecipeFilter(request.GET, queryset=recipe_list)

    context = {
        "recipe_list": recipe_list,
        'filter': recipe_filter,
    }
    return render(request, 'recipe/recipe_list.html', context=context)


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    context = {
        "recipe": recipe,
    }
    return render(request, 'recipe/recipe_detail.html', context=context)
