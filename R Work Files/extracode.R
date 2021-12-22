zom = read.csv(file.choose())
str(zom)
table(zom$Country.Code)

summary(lm(zom$Votes ~ zom$Average.Cost.for.two))

zom.us = subset(zom, zom$Country.Code == 216)
table(zom.us$Country.Code)

library(summarytools)
descr(cbind("votes" = zom.us$Votes, "avg.cost" = zom.us$Average.Cost.for.two))
summary(lm(zom.us$Votes ~ zom.us$Average.Cost.for.two))

zom.can = subset(zom, zom$Country.Code == 37)
table(zom.can$Country.Code)
descr(cbind("votes" = zom.can$Votes, "avg.cost" = zom.can$Average.Cost.for.two))
summary(lm(zom.can$Votes ~ zom.can$Average.Cost.for.two))

zom.ind = subset(zom, zom$Country.Code == 1) 
table(zom.ind)
descr(cbind("votes" = zom.ind$Votes, "reservation" = zom.ind$Has.Table.booking))
summary(lm(zom.ind$Votes ~ zom.ind$Has.Table.booking))
zom.ind$Has.Table.booking
