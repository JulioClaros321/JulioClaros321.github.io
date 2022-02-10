# Julio Claros LAB 9

########################

########################
# Question 4 - Heavy metal bands by nation
# data from Kaggle: https://www.kaggle.com/mrpantherson/metal-by-nation 

# Q4
# data prep
install.packages("summarytools")
library(summarytools)
install.packages("car")
library(car)
metal <- read.csv(file.choose())
str(metal)
freq(metal$origin, order="freq")
# top 5: USA, Sweden, Germany, United Kingdom, Finland
# subset by the top 5
metal6 <- subset(metal, metal$origin=="Sweden" | 
                        metal$origin=="Germany" | 
                        metal$origin=="United Kingdom" | 
                        metal$origin=="Finland" |
                        metal$origin=="France" |
                        metal$origin=="Norway")

# drop excess factor levels carried over
metal6$origin <- droplevels(metal6$origin)
freq(metal6$origin, order="freq")

mean(metal6$fans[metal6$origin == "Finland"])
sum(metal6$fans[metal6$origin == "Finland"])
mean(metal6$fans[metal6$origin == "France"])
sum(metal6$fans[metal6$origin == "France"])
mean(metal6$fans[metal6$origin == "Germany"])
sum(metal6$fans[metal6$origin == "Germany"])
mean(metal6$fans[metal6$origin == "Norway"])
sum(metal6$fans[metal6$origin == "Norway"])
mean(metal6$fans[metal6$origin == "Sweden"])
sum(metal6$fans[metal6$origin == "Sweden"])
mean(metal6$fans[metal6$origin == "United Kingdom"])
sum(metal6$fans[metal6$origin == "United Kingdom"])

qqPlot(metal6$fans[residuals(metal6.aov)])

metal6.aov = aov(metal6$fans ~ metal6$origin)
summary(metal6.aov)

metal6.welch = oneway.test(metal6$fans ~ metal6$origin)

kruskal.test(metal6$fans ~ metal6$origin)

#4D
TukeyHSD(metal6.aov)

# 4f
summary(metal6.aov)
# SS between/ SStotal = R^2


# 4h 
install.packages("pwr")
library("pwr")
pwr.anova.test(k = 6, f = .08, sig.level = .05, n = 828)

########################
# Question 5
# setup Star Wars data
# https://fivethirtyeight.com/features/americas-favorite-star-wars-movies-and-least-favorite-characters/
# https://github.com/fivethirtyeight/data/tree/master/star-wars-survey
# cleaned separately in Excel

library(readxl)
sw <- read_excel(file.choose(),sheet="data") # StarWars_clean.xlsx
str(sw)
# make a variable if a fan of Star Wars & Star Trek or not
table(Trek=sw$FanStarTrek, Wars=sw$SWFan)
sw$FanOf <- ifelse(sw$FanStarTrek=="Yes" & sw$SWFan=="Yes","Both",
            ifelse(sw$FanStarTrek=="No" & sw$SWFan=="Yes","Wars-Only",
            ifelse(sw$FanStarTrek=="Yes" & sw$SWFan=="No","Trek-Only",
            ifelse(sw$FanStarTrek=="No" & sw$SWFan=="No","Neither", NA))))

# scale of how many Star Wars movies seen
sw$SeenNum<-sw$SeenEp1+sw$SeenEp2+sw$SeenEp3+sw$SeenEp4+sw$SeenEp5+sw$SeenEp6
summary(sw$SeenNum)

### END ###