import sqlite3


db = sqlite3.connect('movie.sqlite')
cur = db.cursor()

cur.execute('SELECT `original_title`, `release_date`, `popularity` FROM `movies`;')
movies = cur.fetchall()
for movie in movies:
    print(movie)
cur.execute('SELECT COUNT(*) FROM `movies` WHERE `popularity` > 700 AND `budget` > 158000000')
count_popul = cur.fetchall()
print(count_popul)

cur.execute('SELECT AVG(`budget`) FROM `movies`;')
avg_bud = cur.fetchall()
print(f'Average film budget is ${round(avg_bud[0][0], 2)}')

cur.execute('SELECT MIN(`budget`) FROM `movies`;')
min_bud = cur.fetchall()
print(min_bud[0][0])
cur.execute('SELECT MAX(`budget`) FROM `movies`;')
maks_bud = cur.fetchall()
print(maks_bud[0][0])
cur.execute('SELECT MAX(`budget`), MIN(`budget`), AVG(`budget`) FROM `movies`;')
budgets = cur.fetchall()
print(f'the max budget is ${budgets[0][0]}')
print(f'the min budget is ${budgets[0][1]}')
print(f'Average film budget is ${round(budgets[0][2], 2)}')

cur.execute('SELECT `id`, `name` FROM `directors` WHERE `name` LIKE "A%";')
direct = cur.fetchall()
print(direct)

cur.execute('SELECT `id`, `name` FROM `directors` WHERE `name` LIKE "%and";')
direct = cur.fetchall()
print(direct)

cur.execute('SELECT `id`, `name` FROM `directors` WHERE `name` LIKE "%ric%";')
direct = cur.fetchall()
print(direct)

cur.execute('SELECT `id`, `name` FROM `directors` WHERE `name` LIKE "%Nick%" OR `name` LIKE "%Jackson%";')
direct = cur.fetchall()
print(direct)