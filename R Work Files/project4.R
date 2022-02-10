#Julio Claros
#Project 4

#Summary Tookls for descr function
library(summarytools)
#Database
movies = read.csv(file.choose())

#Subset for USA movies Only, Remove Na's
usa_movies = na.omit(subset(movie, country == "USA"))

#Summary Statistics Table
descr(cbind("movies_ratings" = usa_movies$imdb_score,
            "movies_duration" = usa_movies$duration,
            "movies_actor_one" = usa_movies$actor_1_facebook_likes,
            "movies_actor_two" = usa_movies$actor_2_facebook_likes,
            "movies_likes"= usa_movies$movie_facebook_likes))

#Check structure of variables
str(usa_movies$actor_1_facebook_likes)
str(usa_movies$movie_facebook_likes)
str(usa_movies$duration)
str(usa_movies$imdb_score)
str(usa_movies$actor_2_facebook_likes)



#Boxplot to check outliers in DV (DV contains outliers but nothing extreme)
boxplot(usa_movies$imdb_score, horizontal = T, xlab= "IMDB Score (Out of 10)")

#Regression Model
movie_model = lm(formula = imdb_score ~ duration + actor_1_facebook_likes + 
                   actor_2_facebook_likes + movie_facebook_likes, data = usa_movies)

summary(movie_model)

#Regression Diagnostics
par(mfrow =c(2, 2))
plot(movie_model)
par(mfrow =c(1,1))


#For Stargazer plot
library(stargazer)
stargazer(movie_model, type = "html", out = "movie_model.html")

#Extra Credit
install.lpackages("tidyverse")
#For GG Plot
library(tidyverse)

#Plot 1
movie_plot = ggplot(usa_movies, aes(x = actor_1_facebook_likes, y = imdb_score, color = duration)) + 
              geom_point() + geom_abline()

print(movie_plot + ggtitle("Actor One Facebook likes on IMDB Scores based on Movie Duration"))

#Plot 2
movie_plot_2 = ggplot(usa_movies, aes(x = movie_facebook_likes, y = imdb_score, color = duration)) + 
              geom_point() + geom_abline()

print(movie_plot_2 + ggtitle("Movie Facebook likes on IMDB Scores based on Movie Duration"))