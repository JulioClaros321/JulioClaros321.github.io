#Julio Claros

villan = c("Auto", "VIKI", "WOPR", "Ultron", "Master Control Program", "The Machines", "Skynet", "HAL")
movie = c("Wall-E", "I Robot", "Wargames", "Avengers: The Age of Ultron", "Tron", "The Matrix", "The Terminator", "2001: A Space Odyssey")
year = c(2008, 2004, 1983, 2015, 1982, 1999, 1984, 1968)
evilai = data.frame(villan, movie, year); evilai
evilai2= data.frame(villan, movie, year, stringsAsFactors = FALSE)
str(evilai)
str(evilai2)

airbag  = read.csv(file.choose()); airbag
str(airbag)

#3c Lab 2: Total number of missing obersvations in injserverity
sum(is.na(airbag$injSeverity))

table(airbag$injSeverity)
library(car)

airbag$ik = recode(airbag$injSeverity, "1=1; 2=2; 3:4 = 3.5; 5=5; 6=6; NA=NA;")
airbag$injSeverity
airbag$ik

airbag$ik = ifelse(airbag$injSeverity==3, 3.5, ifelse(airbag$injSeverity==4, 3.5, airbag$injSeverity))
airbag$ik
table(airbag$injSeverity)
prop.table(table(airbag$injSeverity))*100

load(file.choose())

table(gss$HRS1)
str(gss$HRS1)
class(gss$HRS1)


gss$hours_worked = as.character(gss$HRS1)
gss$hours_worked
gss$hours_worked[gss$hours_worked == "89+ hrs"] = "89"
gss$hours_worked = as.numeric(gss$hours_worked)
gss$hours_worked

gss$hours_worked2 = cut(gss$hours_worked, breaks =  c(-Inf, 39, 40, Inf))
gss$hours_worked2 = ifelse(gss$hours_worked <= 39, 1, ifelse(gss$hours_worked == 40, 2,ifelse(gss$hours_worked >40, 3, gss$hours_worked)))
gss$hours_worked2 = recode(gss$hours_worked, "lo:39=1; 40=2; 41:hi=3")
table(gss$hours_worked2)
prop.table(table(gss$hours_worked2))
