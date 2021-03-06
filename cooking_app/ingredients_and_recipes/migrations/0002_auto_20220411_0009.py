# Generated by Django 3.2.7 on 2022-04-10 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients_and_recipes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forhowmanypersons', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingredients_and_recipes.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='EatingCathegory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('time', models.TimeField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(max_length=255)),
                ('eatings', models.ManyToManyField(to='ingredients_and_recipes.Eating', verbose_name='list of eating')),
            ],
        ),
        migrations.AddField(
            model_name='eating',
            name='eatingcathegory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingredients_and_recipes.eatingcathegory'),
        ),
    ]
