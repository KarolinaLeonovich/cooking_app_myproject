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


# #with postgres base
# import psycopg2
#
#
# conn = psycopg2.connect(
#     host="localhost",
#     database="recipes",
#     user="postgres",
#     password="12345")
#
# cursor = conn.cursor()

# cursor.execute('''select * from ingredients_and_recipes_ingredient''')
#
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
#                            VALUES (%s,%s,%s,%s,%s)''', (row[0], row[1], row[2], row[3], row[4]))
#             conn.commit()

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


import requests
from bs4 import BeautifulSoup

from ingredients_and_recipes.models import IngredientQuantity

page = requests.get("https://povar.ru/recipes/salat_granatovyi-73167.html")
soup = BeautifulSoup(page.text, "html.parser")
name_rus = soup.find("h1", attrs={"class": "detailed", "itemprop": "name"})
print(name_rus.get_text())
ingr = soup.find_all("li", attrs={"itemprop": "recipeIngredient"})
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
            if lit.isdigit() and iden < 5:
                quantity_num += lit
            else:
                quantity_measure += lit
        quantity_num = int(quantity_num)

        IngredientQuantity.objects.create(ingredient=name_and_quantity[0], quantity_gr=quantity_num, measure=quantity_measure, annotation=quantity_annotation)
    else:
        quantity_annotation = name_and_quantity[1]


how_to_cook = soup.find_all("div", attrs={"class": "detailed_step_description_big"})
h_t_c = ""
for i in how_to_cook:
    h_t_c += i.get_text()
    h_t_c += " "
print(h_t_c)