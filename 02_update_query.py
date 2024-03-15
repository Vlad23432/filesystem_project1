import sqlite3

conn = sqlite3.connect('new_db.sqlite')

conn.execute(' UPDATE `users` SET `phone` = "<+375291234567>" WHERE `id` = 1')

conn.execute(' UPDATE `users` SET `address` = "<Park ave 16, apt. 3>" WHERE `last_name` = "Johns"')
conn.commit()
print(f'Total numer of rows affected: {conn.total_changes}')

c = conn.execute('SELECT * FROM `users`')
for row in c:
    print(row)