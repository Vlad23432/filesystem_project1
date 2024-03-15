import sqlite3

conn = sqlite3.connect('new_db.sqlite')
print('connected')

conn.execute('''CREATE TABLE IF NOT EXISTS `users`
(`id` INT PRIMARY KEY NOT NULL,
`first_name` TEXT NOT NULL,
`last_name` TEXT NOT NULL, 
`phone` TEXT NOT NULL,
`age` INT NOT NULL, 
`address` CHAR(50)
);''')
print('created table')

conn.execute('''INSERT INTO `users` (`id`,`first_name`, `last_name`, `phone`, `age`, `address`)
VALUES(3,'Paul', 'Laeeeedf', '+375001110000', 22, 'Pol st. 22, apt 67')''')
conn.execute('''INSERT INTO `users` (`id`, `first_name`, `last_name`, `phone`, `age`, `address`)
VALUES(4, 'Kelly', 'Johns', '+357229994444', 29, 'Pol st. 8, apt 28' )''')
conn.execute('''INSERT INTO `users` (`id`, `first_name`, `last_name`, `phone`, `age`, `address`)
VALUES(5, 'Kelfe', 'duas', '+753003334455', 90, 'jupiter st. 12 suite 22')''')
conn.commit()