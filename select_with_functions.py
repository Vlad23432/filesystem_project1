import sqlite3

con = sqlite3.connect('movie.sqlite')
cur = con.cursor()

with open('joins.sql', 'r') as file:
    query = file.read()

cur.execute(query)
all_directors_and_movies = cur.fetchall()
print(all_directors_and_movies)