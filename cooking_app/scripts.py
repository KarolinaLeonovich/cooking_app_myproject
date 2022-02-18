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