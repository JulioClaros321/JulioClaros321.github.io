load(file.choose()) 

str(subset(gss, select = c(RINCOM16, SEX, EDUC, POLVIEWS)))

gss$inc = as.numeric(gss$RINCOM16)
gss$fem = as.numeric(gss$SEX)
gss$edu = as.numeric(gss$EDUC)
gss$pol = as.numeric(gss$POLVIEWS) 

summary(lm(inc ~ fem + edu + pol, data = gss)) 
