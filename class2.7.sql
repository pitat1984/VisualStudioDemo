CREATE TABLE movies (
    movie_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(120),
    year INTEGER,
    director VARCHAR(120)
);

CREATE TABLE directors(
    director_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(120),
    last_name VARCHAR (120),
    country VARCHAR (120)
);

DROP TABLE movies

CREATE TABLE movies (
    movie_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(120),
    year INTEGER,
    director_id INTEGER,
    FOREIGN KEY (director_id) REFERENCES directors(director_id)
);

SELECT title FROM movies;

SELECT title, year FROM movies ORDER BY year ASC;

INSERT INTO directors (first_name, last_name, country) VALUES ('Jean-Pierre', 'Jeunet', 'France');

SELECT director_id FROM directors WHERE last_name = 'Jeunet';

INSERT INTO movies (title, year, director_id) VALUES ('Amelie', 2001, 2);

SELECT * FROM directors ORDER BY country ASC;

SELECT directors.country FROM directors INNER JOIN movies ON movies.title='Amelie';

SELECT movies.title, directors.first_name, directors.last_name FROM movies INNER JOIN directors ON movies.director_id=directors.director_id ORDER BY directors.director_id ASC;
