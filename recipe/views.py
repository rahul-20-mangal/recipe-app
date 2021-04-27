from django.shortcuts import render, get_object_or_404, redirect
from recipe.models import Recipe, Ingredient, Collection
from recipe.filters import RecipeFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.db import transaction
from django.contrib.auth.decorators import login_required
from recipe.forms import RecipeForm, IngredientForm, CollectionForm
from django.forms import formset_factory


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


@transaction.atomic
@login_required
def add_recipe(request):
    IngredientFormSet = formset_factory(IngredientForm, extra=5)

    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, request.FILES)
        ingredient_formset = IngredientFormSet(request.POST)

        if recipe_form.is_valid() and ingredient_formset.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.save()

            for ingredient_form in ingredient_formset:
                ingredient = ingredient_form.save(commit=False)
                ingredient.recipe = recipe
                ingredient.save()

            return redirect('recipe:list')

    else:
        recipe_form = RecipeForm()
        ingredient_formset = IngredientFormSet()

    context = {
            "recipe_form": recipe_form,
            "ingredient_formset": ingredient_formset,
    }
    return render(request, 'recipe/add_recipe.html', context=context)


@transaction.atomic
@login_required
def edit_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe_form = RecipeForm(request.POST or None, instance=recipe)

    ingredient = Ingredient.objects.filter(recipe=recipe)
    IngredientFormSet = formset_factory(IngredientForm, extra=5)
    ingredient_formset = IngredientFormSet(request.POST or None)

    if recipe_form.is_valid() and ingredient_formset.is_valid():
        recipe = recipe_form.save(commit=False)
        recipe.author = request.user
        recipe.save()

        for ingredient_form in ingredient_formset:
                ingredient = ingredient_form.save(commit=False)
                ingredient.recipe = recipe
                ingredient.save()
            
        return redirect('recipe:detail', pk=pk)
    
    context = {
        "recipe_form": recipe_form,
        "ingredient_formset": ingredient_formset,
    }
    return render(request, 'recipe/add_recipe.html', context)


@transaction.atomic
@login_required
def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.delete()

    return redirect('recipe:list')


@transaction.atomic
@login_required
def create_collection(request):
    form = CollectionForm(request.POST or None)
    
    if form.is_valid():
        collection = form.save(commit=False)
        collection.user = request.user
        collection.save()
        return redirect('recipe:my-collection')

    context = {
        "form": form,
    }
    return render(request, 'recipe/create_collection.html', context=context)


@login_required
def my_collection(request):
    recipe_list = Recipe.objects.filter(author=request.user)
    
    context = {
        "recipe_list": recipe_list,
    }
    return render(request, 'recipe/my_collection.html', context=context)