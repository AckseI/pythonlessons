import sqlite3
"""
Написать функцию, которая принимает наименование
таблицы и выводит количество одинаковых значений в её полях и наиболее часто повторяющееся значение полей.
"""
conn = sqlite3.connect('lybrarydb-sqlite2.db')
cursor = conn.cursor()

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS Users (
#     id INTEGER PRIMARY KEY,
#     username TEXT NOT NULL,
#     age INTEGER
#     )
# """)
# #
# cursor.execute("""
#     INSERT INTO Users (username, age)
#     VALUES ('Egor','20'),
#     ('Kostya','19'),
#     ('Nikita','19'),
#     ('Kirill','20'),
#     ('Anna','20'),
#     ('Oleg','20'),
#     ('Daniil','20'),
#     ('Grisha','20'),
#     ('Netu','20'),
#     ('Max','20'),
#     ('Alex','20'),
#     ('Melmon','20'),
#     ('Gloria','20'),
#     ('Shkiper','20'),
#     ('Kavalski','20'),
#     ('Riko','20'),
#     ('Obratny Tresh','20'),
#     ('Barry Alen','20'),
#     ('Oliver Queen','20')
# """)

cursor.execute("""
SELECT age FROM Users
""")

results = cursor.fetchall()

ages = [row[0] for row in results]

max_count = ages.count(max(ages, key=lambda i: ages.count(i)))

res = {i for i in ages if ages.count(i) == max_count}

print(max_count, res)

#conn.commit()
conn.close()
