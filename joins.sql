SELECT movies.title, directors.name
FROM movies
INNER JOIN directors
ON movies.director_id = directors.id;