USE movies;

#How much total revenue did comedy movies bring in?

DROP VIEW IF EXISTS comedy_total_revenue;
CREATE VIEW comedy_total_revenue AS
SELECT COUNT(title) AS Total_Comedy_Movies, FORMAT(SUM(revenue), 2) AS Total_Revenue 
FROM movies.titles
	INNER JOIN movies.genre 
		ON titles.movie_id = genre.movie_id
	INNER JOIN movies.financial_info
		ON titles.id = financial_info.id
WHERE genre LIKE "%comedy%";

SELECT * FROM comedy_total_revenue;

#Question: What Are the top 5 most popular movies

DROP VIEW IF EXISTS top_five_movies;
CREATE VIEW top_five_movies AS
SELECT title, 
	   popularity
FROM movies.titles JOIN movies.ratings 
	ON titles.id = ratings.id
ORDER BY popularity DESC
LIMIT 5;

SELECT * FROM top_five_movies;

#Question: What was the average rating of all movies?

DROP VIEW IF EXISTS popularity_average;
CREATE VIEW popularity_average AS
SELECT COUNT(title) AS total_movies_used, 
		AVG(popularity) AS Average_Popularity
FROM movies.titles JOIN movies.ratings
	ON titles.id = ratings.id;

SELECT * FROM popularity_average;

#Question: Are movies longer than the average runtime more popular than movies shorter than the average? 

SELECT COUNT(title) AS titles, 
	   AVG(popularity) Average_popularity
FROM movies.titles
	INNER JOIN movies.movie_summary
		ON titles.movie_id = movie_summary.movie_id
	INNER JOIN movies.ratings
		ON titles.id = ratings.id
WHERE runtime < (SELECT AVG(runtime)
				 FROM movies.movie_summary)
UNION ALL
SELECT COUNT(title) AS titles, AVG(popularity) AS Average_popularity
FROM movies.titles
INNER JOIN movies.movie_summary
	ON titles.movie_id = movie_summary.movie_id
INNER JOIN movies.ratings
	ON titles.id = ratings.id
WHERE runtime > (SELECT AVG(runtime)
				 FROM movies.movie_summary);

#What is the highest grossed movie and who are the actors associated with this movie
DROP VIEW IF EXISTS top_movie_actors;
CREATE VIEW top_movie_actors AS
SELECT title, 
	   revenue, 
       leading_actor
FROM titles 
	JOIN financial_info 
		ON titles.id = financial_info.id
	LEFT JOIN movie_crew 
		ON titles.imdb_id = movie_crew.imdb_id
ORDER BY revenue DESC
LIMIT 1;

SELECT * FROM top_movie_actors;

# What was the net revenue of the movie Tom and Huck
SELECT title, 
	   FORMAT(revenue, 2) AS revenue
FROM titles 
LEFT JOIN financial_info 
	ON titles.id = financial_info.id
LEFT JOIN ratings 
	ON titles.id = ratings.id
WHERE title  = 'tom and huck';
  
# What was the highest grossing movie before the year 2000

DROP VIEW IF EXISTS before_2000;
CREATE VIEW before_2000 AS
SELECT title, 
	   FORMAT(revenue, 2) AS revenue, 
       release_date
FROM titles 
LEFT JOIN financial_info 
	ON titles.id = financial_info.id
LEFT JOIN production_company 
	ON titles.imdb_id = production_company.imdb_id
WHERE release_date < "2000-01-01"
ORDER BY revenue DESC
LIMIT 1;

SELECT * FROM before_2000;

# Which director of the lowest grossing movies

SELECT titles.id, 
	   financial_info.id, 
       movie_crew.director, 
       financial_info.revenue
FROM ((titles
INNER JOIN financial_info 
	ON titles.id =financial_info.id )
INNER JOIN movie_crew 
	ON movie_crew.imdb_id = titles.imdb_id)
WHERE financial_info.revenue = 0
ORDER BY financial_info.revenue;

# Which director had the largest grossing mobie

SELECT titles.id, 
	   financial_info.id, 
       movie_crew.director, 
       FORMAT(financial_info.revenue, 2) AS revenue
FROM ((titles
INNER JOIN financial_info 
	ON titles.id =financial_info.id )
INNER JOIN movie_crew 
	ON movie_crew.imdb_id = titles.imdb_id)
WHERE financial_info.revenue IN (SELECT MAX(financial_info.revenue) 
								 FROM financial_info)
ORDER BY financial_info.revenue DESC;


# Which Production produced the most movies
DROP VIEW IF EXISTS top_prod_comp;
CREATE VIEW top_prod_comp (no_movies, production_company)
AS SELECT COUNT(*)  no_movies, 
		  production_company.prod_comp
FROM production_company
GROUP BY production_company.prod_comp
ORDER BY no_movies DESC;

SELECT * FROM top_prod_comp
LIMIT 1;





