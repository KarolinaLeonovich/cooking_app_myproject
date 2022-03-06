# Generated by Django 3.2.7 on 2022-03-06 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients_and_recipes', '0007_ingredientquantity_recipe_belong_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredientquantity',
            name='recipe_belong_to',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredient_quantity',
            field=models.ManyToManyField(to='ingredients_and_recipes.IngredientQuantity', verbose_name='list of ingredients'),
        ),
    ]