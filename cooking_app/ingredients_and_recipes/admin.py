from django.contrib import admin
from .models import *


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'calories_per_100_gr',
        'protein_per_100_gr',
        'fat_per_100_gr',
        'carbohydrates_per_100_gr',
        "cup250sm",
        "bigspoon",
        "littlespoon",
        "onepiece",
    )


@admin.register(IngredientQuantity)
class IngredientQuantityAdmin(admin.ModelAdmin):
    # list_display = (
    #     'ingredient',
    #     'quantity_gr',
    #     'measure',
    #     'annotation',
    #     'recipe_belong_to',
    # )

    def has_module_permission(self, request):
        return False


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(EatingCathegory)
class EatingCathegoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'time',
    )


@admin.register(Eating)
class EatingAdmin(admin.ModelAdmin):
    list_display = (
        'eatingcathegory',
        'dish',
        'forhowmanypersons',
    )


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    pass
