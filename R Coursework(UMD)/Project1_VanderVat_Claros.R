#Project 1
#Jacob VanderVat and Julio Claros

# data & packages setup
load(file.choose())  # select the full GSS 1972 to 2016 file
library(car)  # needed for recode function
#library(DescTools)  # for effect size
library(summarytools)
#Library for CrammerV function
install.packages("DescTools")
library(DescTools)

#sets gss08 as the base for the data, cuts out all unneeded data
gss08 = subset(gss7216, PRES08 == "Obama" | PRES08 == "McCain" | PRES08 == "OTHER CANDIDATE (SPECIFY)" | PRES08 == "DIDN'T VOTE")

#creates levels for splitting
agegrouped.lev = c("18 to 24", "25 to 34", "35 to 44",
                          "45 to 54", "55 to 64", "65 to 74", "75+")
#makes the ages numbered varibles where 1 = 18 ... 72 = 89+
gss08$agenum = as.numeric(as.character(gss08$AGE))
summary(gss08$agenum)

#recodes the ages into new groups
gss08$agegrouped = factor(ifelse(gss08$agenum < 25, 1,
                                 ifelse(gss08$agenum >=25 & gss08$agenum < 35, 2,
                                    ifelse(gss08$agenum >= 35 & gss08$agenum < 45, 3,
                                     ifelse(gss08$agenum >= 45 & gss08$agenum < 55, 4,
                                        ifelse(gss08$agenum >= 55 & gss08$agenum < 65, 5,
                                          ifelse(gss08$agenum >= 65 & gss08$agenum < 75, 6,
                                                 ifelse(gss08$agenum >= 75, 7, NA))))))),
                          labels = agegrouped.lev, ordered = T)

#Table for ages
summarytools::freq(na.omit(gss08$agegrouped))

#Table for how many votes each person got
summarytools::freq(gss08$PRES08)

#Table for ages vs votes
addmargins(table(gss08$PRES08, gss08$agegrouped))

#ChiSquare Value
chisq.test(table(gss08$PRES08, gss08$agegrouped))

#Crammer for Association level
CramerV((table(gss08$PRES08, gss08$agegrouped)))
