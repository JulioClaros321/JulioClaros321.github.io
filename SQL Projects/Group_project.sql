DROP DATABASE IF exists Movies;
CREATE DATABASE Movies;
USE Movies;

DROP TABLE IF exists titles;
CREATE TABLE titles (
	id			INT		NOT NULL,
	movie_id	INT		NOT NULL,
    imdb_id 	VARCHAR(20),
    title		VARCHAR(200) DEFAULT "Unkown Name",
    PRIMARY KEY(id),
    CONSTRAINT UNIQUE(imdb_id),
    CONSTRAINT UNIQUE(movie_id),
    CONSTRAINT UNIQUE(title)
);

DROP TABLE IF exists financial_info;
CREATE TABLE financial_info (
	id			INT,
    budget		INT,
    revenue		INT,
    FOREIGN KEY(id) REFERENCES titles(id)
);

DROP TABLE IF exists genre;
CREATE TABLE genre ( 
	movie_id	INT,
    genre		SET("Action", "Adventure", "Animation",  "Comedy", "Crime", 
    "Drama", "Family", "Fantasy", "History", "Horror", "Romance", "Thriller"),
	FOREIGN KEY(movie_id) REFERENCES titles(movie_id)
);

DROP TABLES IF exists movie_crew;
CREATE TABLE movie_crew ( 
	imdb_id			VARCHAR(20),
    director		VARCHAR(30),
    main_char		VARCHAR(20),
    leading_actor	VARCHAR(20),
    FOREIGN KEY(imdb_id) REFERENCES titles(imdb_id)
    
);
DROP TABLE IF exists ratings;
CREATE TABLE ratings ( 
	id			INT,
	popularity	DECIMAL(9, 4),
    FOREIGN KEY(id) REFERENCES titles(id)
);

DROP TABLE IF exists movie_summary; 
CREATE TABLE movie_summary (
    movie_id	INT,
    overview	VARCHAR(1000),
    adult		CHAR(7),
    runtime		INT,
    FOREIGN KEY(movie_id) REFERENCES titles(movie_id)
);

DROP TABLE IF exists production_company; 
CREATE TABLE production_company ( 
	imdb_id			VARCHAR(20),
    prod_comp		VARCHAR(50),
    prod_country 	VARCHAR(50),
    release_date	DATE,
	FOREIGN KEY(imdb_id) REFERENCES titles(imdb_id)

);


