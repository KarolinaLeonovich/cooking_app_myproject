from django.contrib import admin
from .models import *


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'calories_per_100_gr',
        'protein_per_100_gr',
        'fat_per_100_gr',
        'carbohydrates_per_100_gr'
    )


@admin.register(IngredientQuantity)
class IngredientQuantityAdmin(admin.ModelAdmin):

    def has_module_permission(self, request):
        return False


@admin.register(RecipeCategory)
class RecipeCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category'
    )
