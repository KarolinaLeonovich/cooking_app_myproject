import csv
# #with sqlite3 base
# import sqlite3


# connection = sqlite3.connect("db.fff")
#
# cursor = connection.cursor()
#
# cursor.execute("""select * from sqlite_master
#             where type = 'table'""")
# tables = cursor.fetchall()
#
# for table in tables:
#     print("1")
#     print(table)
#     print(table[1])

# cursor.execute('''SELECT name FROM sqlite_master WHERE type = "table"''')
# k = cursor.fetchall()
# print(k)

# cursor.execute('''SELECT * FROM ingredients_and_recipes_ingredient''')
# k = cursor.fetchall()
# for i in k:
#     s = ''
#     for j in i:
#         s += str(j) + ' '
#     print(s)

# with open('Ingridients.csv', encoding="utf8", newline='') as File:
#     reader = csv.reader(File, delimiter=",")
#     for row in reader:
#             cursor.execute('''INSERT INTO ingredients_and_recipes_ingredient
#                            (name, protein_per_100_gr, fat_per_100_gr, carbohydrates_per_100_gr, calories_per_100_gr)
#                            VALUES (?, ?, ?, ?, ?)''', (row[0], row[1], row[2], row[3], row[4]))
#             connection.commit()
#


#with postgres base
import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="recipes",
    user="postgres",
    password="12345")

cursor = conn.cursor()

cursor.execute('''select * from ingredients_and_recipes_ingredient''')

k = cursor.fetchall()
for i in k:
    s = ''
    for j in i:
        s += str(j) + ' '
    print(s)

with open('Ingridients.csv', encoding="utf8", newline='') as File:
    reader = csv.reader(File, delimiter=",")
    for row in reader:
            cursor.execute('''INSERT INTO ingredients_and_recipes_ingredient
                           (name, protein_per_100_gr, fat_per_100_gr, carbohydrates_per_100_gr, calories_per_100_gr)
                           VALUES (%s,%s,%s,%s,%s)''', (row[0], row[1], row[2], row[3], row[4]))
            conn.commit()

# Grabbing for recipes)

# import requests
# from bs4 import BeautifulSoup
#
# file = open("otus.txt", "w")
# links_list = ["https://povar.ru/list/meat",
#               "https://povar.ru/list/fish",
#               "https://povar.ru/list/ptica",
#               "https://povar.ru/list/vegies",
#               "https://povar.ru/list/salad",
#               "https://povar.ru/list/soup",
#               "https://povar.ru/list/vypechka",
#               "https://povar.ru/list/dessert"]
# pages_list = [348, 204, 346, 635, 208, 129, 533, 111]
# for i, p in enumerate(links_list):
#     for q in range(pages_list[i]):
#         link = f'{p}' + "/" + f"{q}"
#         page = requests.get(link)
#         soup = BeautifulSoup(page.text, "html.parser")
#         for link in soup.find_all('a', attrs={"class": "listRecipieTitle"}):
#             a = link.get('href')
#             file.write("https://povar.ru" + str(a) + "\n")
# file.close()



from time import sleep
import random
import requests
from bs4 import BeautifulSoup
from ingredients_and_recipes.models import IngredientQuantity, Ingredient, Recipe
file = open("otus.txt", "r")
lines = file.readlines()
random_int = random.randint(1, 6)
count = 100
link_number = 121 #задаем последний спижженый рецепт
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}
for inx, line in enumerate(lines):
    if inx > link_number:
        print(line)
        if count == 0:
            break
        url = line.strip()
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.text, "html.parser")
        name_ru = soup.find("h1", attrs={"class": "detailed", "itemprop": "name"})
        name_rus = name_ru.get_text().strip()
        ingr = soup.find_all("li", attrs={"itemprop": "recipeIngredient"})
        ingred_array = []
        eng_name1 = url[25:]
        eng_name = eng_name1[:-5]
        for i in ingr:
            line = i.get_text()
            name_and_quantity = line.split('—')
            name_and_quantity[0] = name_and_quantity[0].replace(u'\xa0', u'')
            name_and_quantity[0] = name_and_quantity[0].strip()
            name_and_quantity[1] = name_and_quantity[1].replace(u'\xa0', u'')
            quantity_num = ''
            quantity_measure = ""
            quantity_annotation = ""
            if name_and_quantity[1][0].isdigit():
                for iden, lit in enumerate(name_and_quantity[1]):
                    if not lit.isalpha() and iden < 8:
                        quantity_num += lit
                    else:
                        quantity_measure += lit
                quantity_num = quantity_num.replace(".", "")
                quantity_num = quantity_num.replace(",", ".")
                quantity_num = quantity_num.replace(" ", "")
                quantity_num = quantity_num.replace("(", "")
                quantity_num = quantity_num.replace('\\', "/")
                if "/" in quantity_num and '-' in quantity_num:
                    quantity_num_array3 = quantity_num.split("-")
                    quantity_num_array3_1 = quantity_num_array3[0].split("/")
                    quantity_num_array3_2 = quantity_num_array3[1].split("/")
                    quantity_num_3_1 = float(quantity_num_array3_1[0]) / float(quantity_num_array3_1[1])
                    quantity_num_3_2 = float(quantity_num_array3_2[0]) / float(quantity_num_array3_2[1])
                    quantity_num = quantity_num_3_1 + quantity_num_3_2 / 2
                elif "/" in quantity_num:
                    quantity_num_array = quantity_num.split("/")
                    num1 = float(quantity_num_array[0])
                    num2 = float(quantity_num_array[1])
                    quantity_num = num1 / num2
                elif '-' in quantity_num:
                    quantity_num_array2 = quantity_num.split("-")
                    num1 = float(quantity_num_array2[0])
                    num2 = float(quantity_num_array2[1])
                    quantity_num = num1 + num2 / 2
                quantity_num = float(quantity_num)
                try:
                    base_name = name_and_quantity[0].capitalize()
                    current_ingredient = Ingredient.objects.get(name=base_name)
                    print("Success!", current_ingredient)
                    temp_var = IngredientQuantity.objects.create(ingredient=current_ingredient, quantity=quantity_num,
                                                      measure=quantity_measure, annotation=quantity_annotation)
                    ingred_array.append(temp_var)
                except:
                    n_a_q = name_and_quantity[0].capitalize()
                    cur_ingredient = Ingredient.objects.create(name=n_a_q)
                    temp_var = IngredientQuantity.objects.create(ingredient=cur_ingredient, quantity=quantity_num,
                                                      measure=quantity_measure, annotation=quantity_annotation)
                    ingred_array.append(temp_var)
            else:
                quantity_annotation = name_and_quantity[1]
        how_to_cook = soup.find_all("div", attrs={"class": "detailed_step_description_big"})
        h_t_c = ""
        for i in how_to_cook:
            h_t_c += i.get_text()
            h_t_c += " "
        portions = soup.find("em", attrs={"itemprop": "recipeYield"})
        try:
            numb_port = int(portions.get_text()[-1])
        except ValueError:
            numb_port = 0
        k = Recipe.objects.create(name=name_rus, eng_name=eng_name, how_to_cook=h_t_c, for_how_many_persons=numb_port)
        k.ingredient_quantity.set(ingred_array)
        sleep(random_int)
        count -= 1
        print(count)

file.close()


#freshlines
from ingredients_and_recipes.models import IngredientQuantity, Recipe
e = IngredientQuantity.objects.all()
e.delete()
r = Recipe.objects.all()
r.delete()

#parcing of measurmants
import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="recipes",
    user="postgres",
    password="12345")

cursor = conn.cursor()

cursor.execute('''select * from ingredients_and_recipes_ingredient''')
row1 = 0
row2 = 0
row3 = 0
row4 = 0
k = cursor.fetchall()
with open('mesurments.csv', encoding="utf8", newline='') as File:
    reader = csv.reader(File, delimiter=",")
    for row in reader:
        for i in k:
            if row[0].lower() == i[1].lower() or (row[0] in i[1]) or (i[1] in row[0]):
                if row[1] != '-':
                    row1 = row[1]
                    row1 = row1.replace(",", ".")
                    row1 = float(row1)
                if row[2] != '-':
                    row2 = row[2]
                    row2 = row2.replace(",", ".")
                    row2 = float(row2)
                if row[3] != '-':
                    row3 = row[3]
                    row3 = row3.replace(",", ".")
                    row3 = float(row3)
                if row[4] != '-':
                    row4 = row[4]
                    row4 = row4.replace(",", ".")
                    row4 = float(row4)
                    print(row[0])
                    print(row1, row2, row3, row4, i[1])
                    print(row[1], row[2], row[3], row[4], i[1])
                    cursor.execute("""UPDATE ingredients_and_recipes_ingredient
                                       SET cup250sm = %s WHERE name = %s""", (row1, i[1]))
                    cursor.execute("""UPDATE ingredients_and_recipes_ingredient
                                       SET bigspoon = %s WHERE name = %s""", (row2, i[1]))
                    cursor.execute("""UPDATE ingredients_and_recipes_ingredient
                                       SET littlespoon = %s WHERE name = %s""", (row3, i[1]))
                    cursor.execute("""UPDATE ingredients_and_recipes_ingredient
                                       SET onepiece = %s WHERE name = %s""", (row4, i[1]))
                    conn.commit()
        row1 = 0
        row2 = 0
        row3 = 0
        row4 = 0



