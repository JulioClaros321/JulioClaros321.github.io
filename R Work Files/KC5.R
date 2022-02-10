load(file.choose())
install.packages("summarytools")
library("summarytools")
library(car)
library(pwr)
pew$edu


summary(pew$edu)

freq(pew$edu)

mean(na.omit(pew$test[pew$edu=="LTHS"]))
mean(na.omit(pew$test[pew$edu=="HS"]))
mean(na.omit(pew$test[pew$edu=="SCol"]))
mean(na.omit(pew$test[pew$edu=="Bach+"]))


boxplot(pew$test~pew$edu)
leveneTest(pew$test~pew$edu, center = mean)


pew.aov = aov(pew$test~pew$edu)
summary(pew.aov)
TukeyHSD(pew.aov)

qqPlot(pew.aov$residuals)

pew.htest = oneway.test(pew$test~pew$edu, var.equal = F)
pairwise.t.test(pew$test, pew$edu, p.adjust.method = "bonferroni")

#Question 9
(3 * (59.912 - 1)) / (3 * (59.912 + 1) + 1055)

pwr.anova.test(k = 4, f = .14, sig.level = .05, n = 89, power = NULL)
pwr.anova.test(k = 4, f = .14, sig.level = .05, power = .8)


