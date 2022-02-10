#Julio Claros
#INST 314 Project

#Summary Tookls for descr function
library(summarytools)
#Database
movies = read.csv(file.choose())

#Database Subset for USA Movies
usa_movies = na.omit(subset(movies, movies$country ==  "USA"))

#Summary Statistics Table
descr(cbind("movies_duration" = usa_movies$duration, "movies_ratings" = usa_movies$imdb_score))

#Boxplot to check outliers in DV (DV contains outliers but nothing extreme)
boxplot(usa_movies$imdb_score, horizontal = T, xlab= "IMDB Score (Out of 10)")



#Standard IV DV Plot with Line of Best Fit
plot(usa_movies$duration, usa_movies$imdb_score,
     pch = 20,
     cex = 1,
     col = "blue",
     main = "Movies Duration vs IMDB Score",
     xlab = "Duration of Movies (mins)",
     ylab = "IMDB Score (out of 10)"
     )
abline(lm(formula = usa_movies$imdb_score ~ usa_movies$duration), col = "red")

#Regression Model
summary(lm(formula = usa_movies$imdb_score ~ usa_movies$duration))
#Correlation Test
cor.test(usa_movies$imdb_score, usa_movies$duration)
#Regression Diagnostic Plots
par(mfrow =c(2, 2))
plot(lm(formula = usa_movies$imdb_score ~ usa_movies$duration))
par(mfrow =c(1,1))

