from django.shortcuts import render, get_object_or_404
from recipe.models import Recipe
from recipe.filters import RecipeFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.db import transaction


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
    

@transaction.atomic
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('recipe:list')
    else:
        form = UserCreationForm()
    return render(request, 'recipe/signup.html', {'form': form})