import sqlite3

conn = sqlite3.connect('new_db.sqlite')

c = conn.execute('SELECT * FROM `users`')
for row in c:
    print(row)

c = conn.execute('SELECT `first_name`, `last_name`, `age` FROM `users`')
for row in c:
    print(f'Name: {row[0]}\nSurname: {row[1]}\nAge: {row[2]}\n')

