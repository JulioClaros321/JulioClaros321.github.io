
# Student Name - 

#install.packages("stats",dependencies = TRUE)
library(readxl)

## Read spreadsheet
childoutlook <- read_excel("C:/Users/Julio/Downloads/R work Files/Lab 4 dataset - childoutlook.xlsx")

# Verify data
print (childoutlook)

##
## Sample size and counts for Yes, No, Not Sure
#
Samplesize <- nrow(childoutlook)
print (Samplesize)
Responses <- table(childoutlook)
print (Responses)
point_estimate = 240/1000
print(point_estimate)

##error 

error = sqrt((point_estimate * (1 - point_estimate))/Samplesize)
print(error)
thing = 1.96 * error
print(thing)
## --------------------------------------------------------------------------------------
## Confidence interval for No responses
## --------------------------------------------------------------------------------------

print (Responses[1])

ttestNo <- prop.test(Responses[1],Samplesize,conf.level = 0.95)
print (ttestNo)

## --------------------------------------------------------------------------------------
## Confidence interval for Yes responses
## --------------------------------------------------------------------------------------

print (Responses[3])

ttestYes <- prop.test(Responses[3],Samplesize,conf.level = 0.95)
print (ttestYes)




