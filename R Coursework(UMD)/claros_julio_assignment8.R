comic = read.csv(file.choose())
comic

marvel = subset(comic, Studio == "Marvel")
dc = subset(comic, Studio == "DC")

#Question 2:
summary(marvel$Worldwide)
length(marvel$Worldwide)
sd(marvel$Worldwide)

summary(dc$Worldwide)
length(dc$Worldwide)
sd(dc$Worldwide)

df = 47 + 25 - 2
sqrt(((393.06^2)/47) + ((401.8^2)/25))
((616.9-526.9)/(sqrt(((393.06^2)/47) + ((401.8^2)/25))))
#Conf = 1.67
t.test(x = dc$Worldwide, y = marvel$Worldwide, alternative = "two.sided", paired = FALSE, conf.level = .9, var.equal = TRUE)
?t.test

.912 / sqrt((1/25) + (1/47))

install.packages("pwr")
library(pwr)
?power.t.test
power.t.test(n = 126, d = .5, sig.level = .05, alternative = "two.sided", type = "two.sample")


lol = power.t.test(n = 126, d = .5, sig.level = .05, alternative = "two.sided", type = "two.sample")
curve(lol)

