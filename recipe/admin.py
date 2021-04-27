from django.contrib import admin
from recipe.models import Recipe, Ingredient, Collection


class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 5   


class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Collection)