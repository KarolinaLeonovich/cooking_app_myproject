from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from ingredients_and_recipes.views import RecipeList, CreateIngredientView, IngredientDetailView, RecipeDetailView, CreateRecipeView, MenuDetailView, CreateMenuView

urlpatterns = [
    path('allrecipes/', RecipeList.as_view(), name='allrecipes'),
    path('ingredients/<int:ing_id>/', IngredientDetailView.as_view(), name='ingredient-detail'),
    #path('ingredients/', IngredientList.as_view(), name='list_of_ingredients'),
    path('newingredient/', CreateIngredientView.as_view()),
    path('newrecipe/', CreateRecipeView.as_view()),
    path('recipes/<int:rec_id>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('menu/<int:menu_id>/', MenuDetailView.as_view(), name='menu-detail'),
    path('newmenu/', CreateMenuView.as_view()),
]
urlpatterns += staticfiles_urlpatterns()
