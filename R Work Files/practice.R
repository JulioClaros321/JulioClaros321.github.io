library(Ecdat)
data(Housing)
table(Housing$bedrooms)
addmargins(table(Housing$bedrooms))

#Number of 3 rooms frequence
(301/546)
round(prop.table(table(Housing$bedrooms)), 3)

#percentage
(301/546)*100
round(prop.table(table(Housing$bedrooms)), 3) * 100

10000/40000000

lol = read.csv("movies.csv", TRUE, ",")
lol
