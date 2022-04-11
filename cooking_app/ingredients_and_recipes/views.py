from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from ingredients_and_recipes.forms import IngredientForm, RecipeForm
from ingredients_and_recipes.models import Recipe, Ingredient, Menu

class RecipeList(ListView):
    model = Recipe
    template_name = 'recipe.html'


class CreateIngredientView(CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'newingredient.html'
    success_url = reverse_lazy('list_of_ingredients')

class CreateRecipeView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'newrecipe.html'
    success_url = reverse_lazy('list_of_ingredients')

class IngredientDetailView(ListView):
    model = Ingredient
    template_name = 'ingredient.html'

    def get_queryset(self):
        if self.kwargs['ing_id'] == 0:
            return Ingredient.objects.all()
        else:
            return Ingredient.objects.filter(id=self.kwargs['ing_id'])


class RecipeDetailView(ListView):
    model = Ingredient
    template_name = 'recipe_detail.html'

    def get_queryset(self):
        if self.kwargs['rec_id'] == 0:
            return Recipe.objects.all()
        else:
            return Recipe.objects.filter(id=self.kwargs['rec_id'])


class MenuDetailView(ListView):
    model = Menu
    template_name = 'menu_detail.html'