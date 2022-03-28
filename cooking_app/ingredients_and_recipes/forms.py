from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Ingredient, Recipe, IngredientQuantity


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'calories_per_100_gr', 'protein_per_100_gr', 'fat_per_100_gr', 'carbohydrates_per_100_gr']

class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ['name', 'eng_name', 'ingredient_quantity', 'how_to_cook', 'for_how_many_persons']
    ingredient_quantity = forms.ModelMultipleChoiceField(
        queryset=IngredientQuantity.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )



# class UserCreateForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#
#     class Meta:
#         model = User
#         fields = ("username", "email", "password", "password2")
#
#     def save(self, commit=True):
#         user = super(UserCreationForm, self).save(commit=False)
#         user.email = self.cleaned_data("email")
#         if commit:
#             user.save()
#         return user


