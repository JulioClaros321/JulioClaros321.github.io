#Julio and Jacob Project 2 R file


kickstart = read.csv(file.choose())

library(car)  # needed for recode function
#library(DescTools)  # for effect size
library(summarytools)
#Library for CrammerV function
install.packages("DescTools")
library(DescTools)
library(reticulate)
py_install("pandas")

#subset functions into objects
food = subset(kickstart, category == "Food")
music = subset(kickstart, category == "Music") 

length(music$usd_pledged_real)
#N of food Pledges
food.numb_pledges = length(food$usd_pledged_real)

#Standard Deviation of Pledges
sd(food$usd_pledged_real)

#N of music pledges
music.numb_pledges = length(music$usd_pledged_real)

#Standard Deviation of Music Pledges
sd(music$usd_pledged_real)

#summary of both DV variables
music_pledge = music$usd_pledged_real
food_pledge = food$usd_pledged_real
max_length = max(length(music_pledge), length(food_pledge))
length(food_pledge) = max_length
length(music_pledge) = max_length 
entire_table = cbind(food_pledge, music_pledge)


#individual data frames
food_table= data.frame(Category = "Food", "Pledged_Amount"= sum(food$usd_pledged_real))
music_table = data.frame(Category = "Music", "Pledged_Amount" = sum(music$usd_pledged_real))

#Combined total money of pledges for IV Frequency Chart
total = rbind(food_table, music_table)
percent_table = cbind(total, "percent" = (prop.table(total$Pledged_Amount)))

#Recode of USD Pledged data into intervals of 5 (in 100,000's)
kickstart$USD_Pledged_Recode <- cut(kickstart$usd_pledged_real,
                                     breaks=c(-1, 1, 2, 3, 4, 5, 10, 45),
                                     labels=c("<1","1-2","2-3","3-4","4-5","5-10",">10"))

#getting pledged data for each category individually
table(kickstart$USD_Pledged_Recode[kickstart$category == "Food"])
table(kickstart$USD_Pledged_Recode[kickstart$category == "Music"])

#Percent and frequency table (Shows us the percent Food makes up out of all the kickstarters)
table(kickstart$category == "Food")
round(prop.table(table(kickstart$category == "Food"))*100, 2)

table(kickstart$category == "Music")
round(prop.table(table(kickstart$category == "Music"))*100, 2)

#Stat summary table broken down in 100,000's individually
table(kickstart$USD_Pledged_Recode[kickstart$category == "Food"])
round(prop.table(table(kickstart$USD_Pledged_Recode[kickstart$category == "Food"]))*100, 2)

table(kickstart$USD_Pledged_Recode[kickstart$category == "Music"])
round(prop.table(table(kickstart$USD_Pledged_Recode[kickstart$category == "Music"]))*100, 2)


#Cohens D
d = abs((xbar - u)/s)#not sure how to do in R but maybe can do in excel
  
#boxplot
boxplot(entire_table)

