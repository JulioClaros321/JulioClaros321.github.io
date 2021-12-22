# INST 314 
#Julio Claros

########################

# Q1 - no setup
install.packages("Hmisc")
library("Hmisc")
regular = c(16, 20, 21, 22, 23, 22, 27, 25, 27, 28)
premium = c(19, 22, 24, 24, 25, 25, 26, 26, 28, 32)

mean(regular)
sd(regular)

mean(premium)
sd(premium)

cov(data.frame(regular, premium))
cor(regular, premium)

(cor(regular, premium))^2
cor.test(regular, premium)
# Q2 - no setup

# Q3 - fix the GOVINFO variable
# import data
load(file.choose()) # import gss_2016.Rdata
# fix the gov info variable
library(car)
install.packages("descr")
library("descr")
gss$govinfo.fix <- car::recode(as.numeric(gss$GOVTINFO),
"3=0; 4=1; 5=10; 6=2; 7=3; 8=4; 9=5; 10=6; 11=7; 12=8; 13=9; else=NA")
descr(gss$govinfo.fix)
# alt. code if car package is not working
gss$govinfo.fix <- ifelse(as.numeric(gss$GOVTINFO)==3,0,
                   ifelse(as.numeric(gss$GOVTINFO)==4,1,
                   ifelse(as.numeric(gss$GOVTINFO)==6,2,
                   ifelse(as.numeric(gss$GOVTINFO)==7,3,
                   ifelse(as.numeric(gss$GOVTINFO)==8,4,
                   ifelse(as.numeric(gss$GOVTINFO)==9,5,
                   ifelse(as.numeric(gss$GOVTINFO)==10,6,
                   ifelse(as.numeric(gss$GOVTINFO)==11,7,
                   ifelse(as.numeric(gss$GOVTINFO)==12,8,
                   ifelse(as.numeric(gss$GOVTINFO)==13,9,
                   ifelse(as.numeric(gss$GOVTINFO)==5,10,NA)))))))))))
# check recode
descr(gss$govinfo.fix) # GSS site: median=6, mean=6.13, sd=2.59
table(as.numeric(gss$GOVTINFO))
table(gss$govinfo.fix)

summary(as.numeric(gss$CORRUPT2))
sd(as.numeric(na.omit(gss$CORRUPT2)))
sum(as.numeric(na.omit(gss$CORRUPT2)))
    
summary(as.numeric(gss$POLEFF17))
sd(as.numeric(na.omit(gss$POLEFF17)))
sum(as.numeric(na.omit(gss$POLEFF17)))

summary(as.numeric(gss$MAKEJOBS))
sd(as.numeric(na.omit(gss$MAKEJOBS)))
sum(as.numeric(na.omit(gss$MAKEJOBS)))

summary(as.numeric(gss$SAVEJOBS))
sd(as.numeric(na.omit(gss$SAVEJOBS)))
sum(as.numeric(na.omit(gss$SAVEJOBS)))

summary(as.numeric(gss$HLPHITEC))
sd(as.numeric(na.omit(gss$HLPHITEC)))
sum(as.numeric(na.omit(gss$HLPHITEC)))

summary(as.numeric(gss$govinfo.fix))
sd(as.numeric(na.omit(gss$govinfo.fix)))
sum(as.numeric(na.omit(gss$govinfo.fix)))

cor(as.numeric(gss$CORRUPT2), as.numeric(gss$POLEFF17), use = "complete.obs", method = "pearson")
cor.test(as.numeric(gss$CORRUPT2), as.numeric(gss$POLEFF17))

gss$corrupt = as.numeric(gss$CORRUPT2)
gss$pole = as.numeric(gss$POLEFF17)
gss$makejobs = as.numeric(gss$MAKEJOBS)
gss$savejobs = as.numeric(gss$SAVEJOBS)
gss$hlph = as.numeric(gss$HLPHITEC)
gss$govinfo = as.numeric(gss$govinfo.fix)

gss.mat = gss[,c("corrupt", "pole", "makejobs", "savejobs", "hlph", "govinfo")]
rcorr(as.matrix(gss.mat))
round((gss.mat), 3)

plot(jitter(gss$corrupt), jitter(gss$pole))
### END ###
