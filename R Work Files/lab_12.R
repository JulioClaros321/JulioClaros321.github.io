#Julio Claros 
#Lab 12

library(summarytools)  # for summarytools
library(car)  # for recode & scatterplot
library(pwr)  # for power: pwr.f2.test

bike <- read.csv(file.choose(), header=T)  # load day.csv

# use starting with Q1a
# un-normalize select variables
bike$atemp.u <- bike$atemp *50
bike$temp.u <- bike$temp *41
bike$hum.u  <- bike$hum *100
bike$wind.u <- bike$windspeed *67
# drop normalized variables so you don't accidentally use them later.
bike[,c("atemp", "temp", "hum", "windspeed")] <- NULL

bike.spring <- subset(bike, bike$season==1)
bike.summer <- subset(bike, bike$season==2)
bike.fall <- subset(bike, bike$season==3)
bike.winter <- subset(bike, bike$season==4)

bike_count = lm(cnt ~ factor(season) + mnth + holiday + workingday + temp.u + hum.u + wind.u, data = bike)
summary(bike_count)

vif(bike_count)

bike_count.spring = lm(cnt ~ season + factor(mnth) + holiday + workingday + temp.u + hum.u + wind.u, data = bike.spring)
summary(bike_count.spring)

bike_count.summer = lm(cnt ~ season + factor(mnth) + holiday + workingday + temp.u + hum.u + wind.u, data = bike.summer)
summary(bike_count.summer)

bike_count.fall = lm(cnt ~ season + factor(mnth) + holiday + workingday + temp.u + hum.u + wind.u, data = bike.fall)
summary(bike_count.fall)

bike_count.winter = lm(cnt ~ season + factor(mnth) + holiday + workingday + temp.u + hum.u + wind.u, data = bike.winter)
summary(bike_count.winter)

bike[469,]


res.spring=summary(lm(cnt~factor(mnth) + holiday + workingday + temp.u + hum.u + wind.u, bike.spring))
summary(res.spring$residuals)


bike$temp.f = (9/5)*bike$temp.u + 32
cor.test(bike$temp.f,  bike$temp.u)
