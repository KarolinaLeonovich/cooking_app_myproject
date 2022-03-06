# Generated by Django 3.2.7 on 2022-03-06 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients_and_recipes', '0008_auto_20220306_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredient_quantity',
            field=models.ManyToManyField(blank=True, null=True, to='ingredients_and_recipes.IngredientQuantity', verbose_name='list of ingredients'),
        ),
    ]