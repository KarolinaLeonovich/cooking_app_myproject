from django.http import request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from ingredients_and_recipes.forms import IngredientForm
from ingredients_and_recipes.models import Recipe, Ingredient


class RecipeList(ListView):
    model = Recipe
    template_name = 'recipe.html'


class IngredientList(ListView):
    model = Ingredient
    template_name = 'ingredient.html'


class CreateIngredientView(CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'newingredient.html'
    success_url = reverse_lazy('list_of_ingredients')


class IngredientDetailView(ListView):
    model = Ingredient
    template_name = 'ingredient2.html'

    def get_context_data(self, **kwargs):
        context = super(IngredientDetailView, self).get_context_data(**kwargs)
        context['ing_id'] = kwargs['ing_id']
        return context


# def show_ingr(request, ing_id):
#     ingridients = Ingredient.objects.all()
#     return render(request,
#                   'ingredient2.html',
#                   context={'ing_id': ing_id, 'ingridients': ingridients})
