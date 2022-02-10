
# Student Name - Julio Claros

#install.packages("stats",dependencies = TRUE)
library(readxl)

## Read spreadsheet
SCF_expense <- read_excel("C:/Users/Julio/Downloads/R work Files/Lab 4 dataset - seneca.xlsx")

# Verrify data
print(SCF_expense)

##
## Plot the time series data
##

plot (SCF_expense$`Period (t)`,SCF_expense$`Expense (%)`,type = "b",main="SCF Expenses",xlab="Time preiod",ylab="Expense %")

## --------------------------------------------------------------------------------------
## Regression - to be changed
## --------------------------------------------------------------------------------------

mylinearmodel <- lm(SCF_expense$`Expense (%)` ~ SCF_expense$`Period (t)`)
summary(mylinearmodel)
anova(mylinearmodel)  ## sum of squares

eight = 13.8 - .7*(8)
print(eight)
13.8 - .7*(9)
13.8 - .7*(10)
13.8 - .7*(11)
13.8 - .7*(12)
13.8 - .7*(13)
