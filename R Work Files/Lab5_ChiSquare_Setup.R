# INST 314
# Lab 5 Setup code
# Chi-Square
# Shawn Janzen 
# last updated 14 Feb 2019

# Q5
# Q5a - no code
# Q5b
# if you have not already installed summary tools, remove the # on line 15 and run line 15 before line 16
# if you cannot install summary tools, then ignore lines below that use summarytools in the command and substitute with other basic functions, such as table() and summary()
#install.packages("summarytools")
library(summarytools)

load(file.choose()) # find & open the 2016 GSS dataset

class(gss$AGE)  # examine how R 'sees' the AGE variable
# 'permanently' convert age from factor to numeric as new variable
gss$age.r = as.numeric(gss$AGE)+17  # add 17, because when converted, age 18 = 1, so add 17 to make 18 = 18, 19=19, etc.
# report summary stats for age by gender
summary(gss$age.r[gss$SEX=="MALE"])
summary(gss$age.r[gss$SEX=="FEMALE"])
sd(gss$age.r[gss$SEX=="MALE"])
sd(gss$age.r[gss$SEX=="FEMALE"])
length(gss$age.r[gss$SEX=="MALE"])-sum(is.na(gss$age.r[gss$SEX=="MALE"])) # n
length(gss$age.r[gss$SEX=="FEMALE"])-sum(is.na(gss$age.r[gss$SEX=="FEMALE"])) # n

# create age groups with each age group = 5 years, plus low and high age caps
gss$age10 = cut(gss$age.r, breaks=c(18,25, #1 18-25
                                    30, #2 26-30
                                    35, #3 31-35
                                    40, #4 36-40 
                                    45, #5 41-45
                                    50, #6 46-50
                                    55, #7 51-55
                                    60, #8 56-60
                                    65, #9 61-65
                                    Inf)) #10 66+
table(gss$AGE, gss$age10)  # confirm recode
summarytools::freq(gss$age10[gss$SEX=="MALE"])  # check summary stats for men
summarytools::freq(gss$age10[gss$SEX=="FEMALE"])  # check summary stats for women
# take a look at the DV: pass good job opportunities for family benefit
# separate the DV by gender
summarytools::freq(gss$FAMORJOB[gss$SEX=="MALE"])  # check summary stats for men
summarytools::freq(gss$FAMORJOB[gss$SEX=="FEMALE"])  # check summary stats for women

# use the following code to create bivariate tables & compute Chi Square for each gender 
tab.job.men = table(gss$FAMORJOB[gss$SEX=="MALE"], gss$age10[gss$SEX=="MALE"])  # store table as an object
tab.job.women = table(gss$FAMORJOB[gss$SEX=="FEMALE"], gss$age10[gss$SEX=="FEMALE"])  #store table as an object

# use these tables to help complete the rest of Q5b.

### End of script ###