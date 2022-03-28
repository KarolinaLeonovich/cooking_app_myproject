from django.db import models

MEASURES_CHOICES =(
    ("стак.", "стак."),
    ("ст.л.", "ст.л."),
    ("чл.", "ч.л."),
    ("гр.", "гр."),
    ("кг.", "кг."),
    ("шт.", "шт."),
    ("пуч.", "пуч."),
    ("зуб.", "зуб."),
    ("щепотк.", "щепотк."),
    ("л.", "л."),
    ("мл.", "мл."),
    ("ломт.", "ломт"),
    ("гол.", "гол."),
    ("вет.", "вет."),
)

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    calories_per_100_gr = models.PositiveIntegerField(blank=True, null=True)
    protein_per_100_gr = models.PositiveIntegerField(blank=True, null=True)
    fat_per_100_gr = models.PositiveIntegerField(blank=True, null=True)
    carbohydrates_per_100_gr = models.PositiveIntegerField(blank=True, null=True)
    cup250sm = models.PositiveIntegerField(blank=True, null=True)
    bigspoon = models.PositiveIntegerField(blank=True, null=True)
    littlespoon = models.PositiveIntegerField(blank=True, null=True)
    onepiece = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class IngredientQuantity(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(blank=True, null=True)
    measure = models.CharField(max_length=255, choices=MEASURES_CHOICES)
    annotation = models.CharField(max_length=255, blank=True)

    def __str__(self):
        if not self.annotation:
            return self.ingredient.name + " - " + str(self.quantity_gr) + " " + self.measure
        else:
            return self.ingredient.name + " " + self.annotation


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    eng_name = models.CharField(max_length=255, blank=True, null=True)
    ingredient_quantity = models.ManyToManyField(IngredientQuantity, verbose_name="list of ingredients")
    how_to_cook = models.TextField()
    for_how_many_persons = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     self.name = self.name.capitalize()
    #     return super(Recipe, self).save(*args, **kwargs)
