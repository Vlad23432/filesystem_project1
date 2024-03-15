import sqlite3

conn = sqlite3.connect('new_db.sqlite')

try:
    conn.execute('''INSERT INTO `users` (`id`,`first_name`, `last_name`, `phone`, `age`, `address`)
    VALUES(6,'test1', 'test1', 'test1', 202, 'test1')''')
    conn.execute('''INSERT INTO `users` (`id`, `first_name`, `last_name`, `phone`, `age`, `address`)
    VALUES(7, 'test2', 'test2', 'test2', 209, 'test2' )''')
except:
    pass
c = conn.execute('SELECT * FROM `users`')
for row in c:
    print(row)

conn.execute('DELETE FROM `users` WHERE `id` = 6;')
c = conn.execute('SELECT * FROM `users`')
for row in c:
    print(row)