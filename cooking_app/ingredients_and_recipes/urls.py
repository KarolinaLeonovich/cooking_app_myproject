from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from ingredients_and_recipes.views import RecipeList, IngredientList, CreateIngredientView, show_ingr

urlpatterns = [
    path('allrecipes/', RecipeList.as_view()),
    path('ingredients/<int:ing_id>/', show_ingr, name='ingredient-detail'),
    path('ingredients/', IngredientList.as_view(), name='list_of_ingredients'),
    path('newingredient/', CreateIngredientView.as_view()),
]
urlpatterns += staticfiles_urlpatterns()
