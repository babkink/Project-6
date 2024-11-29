import sqlite3
import random
from ipaddress import summarize_address_range
from random import randint
from tkinter.tix import Select

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Users(
# id INTEGER PRIMARY KEY,
# username TEXT NOT NULL,
# email TEXT NOT NULL,
# age INTEGER,
# balance INTEGER NOT NULL
# )
# ''')
# cursor.execute('''CREATE INDEX IF NOT EXISTS idx_email ON Users (email)''')
#
# for i in range(10, 110, 10):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
#                    (f'newuser{i/10}', f'test{i/10}@ya.ru', randint(20, 60), 1000))

cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()

# for user in users:
    # if user[0] % 2 != 0:
    #     cursor.execute('UPDATE Users SET balance = ? where ID = ?', (500, user[0]))

# for user in users:
#     if (user[0] - 1) % 3 == 0:
#         print(user)
#         cursor.execute('DELETE FROM Users WHERE id = ?', (f'{user[0]}',))

# for user in users:
#     if user[2] != 60:
#         print(f' Name: {user[1]} | email: {user[2]} | age: {user[3]} | balance: {user[4]}')

# cursor.execute('DELETE FROM users Where id = ?', (6, ))

cursor.execute('SELECT COUNT (*) FROM Users')
count_ = cursor.fetchone()[0]
cursor.execute('SELECT SUM(balance) FROM USers')
sum_ = cursor.fetchone()[0]
print(sum_/count_)
cursor.execute('SELECT AVG(balance) FROM Users')
avg_ = cursor.fetchone()[0]
print(avg_)

connection.commit()
connection.close()