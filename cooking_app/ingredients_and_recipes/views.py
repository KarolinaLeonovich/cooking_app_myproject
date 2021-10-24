from django.http import request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from ingredients_and_recipes.forms import IngredientForm
from ingredients_and_recipes.models import Recipe, Ingredient


class RecipeList(ListView):
    model = Recipe
    template_name = 'recipe.html'


class CreateIngredientView(CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'newingredient.html'
    success_url = reverse_lazy('list_of_ingredients')


class IngredientDetailView(ListView):
    model = Ingredient
    template_name = 'ingredient.html'

    def get_queryset(self):
        if self.kwargs['ing_id'] == 0:
            return Ingredient.objects.all()
        else:
            return Ingredient.objects.filter(id=self.kwargs['ing_id'])