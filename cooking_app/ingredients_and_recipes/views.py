from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView
from ingredients_and_recipes.forms import IngredientForm, RecipeForm, MenuForm
from ingredients_and_recipes.models import Recipe, Ingredient, Menu

class RecipeList(ListView):
    model = Recipe
    template_name = 'recipe.html'


class CreateIngredientView(CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'newingredient.html'

    def get_success_url(self):
        return reverse('allrecipes')

class CreateRecipeView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'newrecipe.html'

    def get_success_url(self):
        return reverse('allrecipes')

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

    def get_queryset(self):
        if self.kwargs['menu_id'] == 0:
            return Menu.objects.all()
        else:
            return Menu.objects.filter(id=self.kwargs['menu_id'])


class CreateMenuView(CreateView):
    model = Menu
    form_class = MenuForm
    template_name = 'newmenu.html'

    def get_success_url(self):
        return reverse('allrecipes')
