import sqlite3
import json

conn = sqlite3.connect('files/librarydb-sqlite.db')
cursor = conn.cursor()

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Users (
# id INTEGER PRIMARY KEY,
# username TEXT NOT NULL,
# email TEXT NOT NULL,
# age INTEGER
# )
# ''')

# cursor.execute("""
#     INSERT INTO Users (username, email, age)
#     VALUES ('Acksel', 'Acksel.com', 20),
#     ('Chiya', 'Chiya.com', 18),
#     ('Smork', 'Smork.com', 21)
#     """)




cursor.execute("""
    SELECT *
    FROM Users
""")

results = cursor.fetchall()

with open('files/new_file.json', 'w') as f:
    json.dump(results, f, indent=2)
    print("New json file is created from data.json file")

#conn.commit()
conn.close()
