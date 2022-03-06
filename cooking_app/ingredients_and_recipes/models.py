from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    calories_per_100_gr = models.PositiveIntegerField(blank=True, null=True)
    protein_per_100_gr = models.PositiveIntegerField(blank=True, null=True)
    fat_per_100_gr = models.PositiveIntegerField(blank=True, null=True)
    carbohydrates_per_100_gr = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Ingredient, self).save(*args, **kwargs)


class RecipeCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        return super(RecipeCategory, self).save(*args, **kwargs)


class IngredientQuantity(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity_gr = models.PositiveIntegerField()
    measure = models.CharField(max_length=255, blank=True)
    annotation = models.CharField(max_length=255, blank=True)


    def __str__(self):
        if not self.annotation:
            return self.ingredient.name + " - " + str(self.quantity_gr)+ " " + self.measure
        else:
            return self.ingredient.name + " " + self.annotation


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    eng_name = models.CharField(max_length=255, blank=True, null=True)
    ingredient_quantity = models.ManyToManyField(IngredientQuantity, verbose_name="list of ingredients")
    how_to_cook = models.TextField()
    for_how_many_persons = models.PositiveSmallIntegerField(blank=True, null=True)
    category = models.ForeignKey(RecipeCategory, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        return super(Recipe, self).save(*args, **kwargs)
