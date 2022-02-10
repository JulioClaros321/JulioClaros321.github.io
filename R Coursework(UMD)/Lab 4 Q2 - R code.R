
# Student Name - Julio Claros

#install.packages("stats",dependencies = TRUE)
library(readxl)

## Read spreadsheet
SAT_GPA <- read_excel("C:/Users/Julio/Downloads/R work Files/Lab 4 dataset - rugglescollege.xlsx")
print(SAT_GPA)
# Verrify data
print(SAT_GPA)

## --------------------------------------------------------------------------------------
## Regression
## --------------------------------------------------------------------------------------

mylinearmodel <- lm(SAT_GPA$`Freshman GPA`~ SAT_GPA$Reading + SAT_GPA$Math)
summary(mylinearmodel)

gpa = -2.671710 + .0043*(660) + .0045*(630)
print(gpa)
