# Generated by Django 3.2.7 on 2022-04-02 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients_and_recipes', '0006_alter_menu_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='data',
            field=models.DateField(),
        ),
    ]
