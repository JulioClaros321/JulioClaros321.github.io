
# Student Name - Julio Claros

#install.packages("stats",dependencies = TRUE)
library(readxl)

## Read spreadsheet
corpbonds <- read_excel("C:/Users/Julio/Downloads/Lab 5 dataset - CorporateBonds.xlsx")

# Verify data
print (corpbonds)

##
## Sample size
#
Samplesize <- nrow(corpbonds)
print (Samplesize)

## --------------------------------------------------------------------------------------
## Confidence interval for maturity
## --------------------------------------------------------------------------------------

# Get mean, standard dev and sample size
sm <- mean(corpbonds$`Years to Maturity`)
my <- mean(corpbonds$Yield)
ssd <- sd(corpbonds$`Years to Maturity`)
sdy <- sd(corpbonds$Yield)
print (sm)
print (ssd)


print(my)
print(sdy)

# For 95% CI.
# alpha = .05 We can get z(alpha/2) = z(0.025) from R:

cl <- 0.95
alpha <- (1 - cl) / 2
tst <-- qnorm (alpha)
me <- tst * ssd /sqrt (Samplesize)
print (cl)
print (alpha)
print (tst)
print (me)

Lowermaturity <- sm - me
Uppermaturity <- sm + me


# See the result
Lowermaturity
Uppermaturity

#yeild 
yeild <- tst * sdy /sqrt (Samplesize)
print(yeild)
lower = my - yeild
upper = my + yeild
print(lower)
print(upper)
