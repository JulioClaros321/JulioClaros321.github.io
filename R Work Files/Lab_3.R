#Julio Claros

?sd

starbucks = read.csv(file.choose(), header = T)
install.packages("plyr")
library("plyr")

install.packages("car") # remove first # sign and run if you need to install the car package, which gives you access to the recode() function
library(car)
# note--I named the Starbucks data as sb.  Change the sb here to whatever you called the Starbucks dataset.
# this code will create a new *fixed* variable called totalfat.
starbucks$totalfat <- starbucks$Total.Fat..g.
starbucks$totalfat <- car::recode(starbucks$totalfat,"'3 2'=3.2") # change "3 2" to 3.2
starbucks$totalfat <- as.numeric(as.character(starbucks$totalfat)) # convert into numeric


summary(starbucks$Sugars..g.)
sd(starbucks$Sugars..g.)
summary(starbucks$Calories)
sd(starbucks$Calories)
summary(starbucks$Trans.Fat..g.)
sd(starbucks$Trans.Fat..g.)
summary(starbucks$totalfat)
sd(starbucks$totalfat)

bev = table(starbucks$Beverage_category)
(bev_table = cbind(bev, frequnecy = round(prop.table(bev), 1)))

aggregate(Calories~Beverage_category, starbucks, mean)

belts = read.csv(file.choose())
belts_table = table(belts$seatbelt, belts$dead)
belts_table
