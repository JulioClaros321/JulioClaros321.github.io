##
## simulate tire mileage 500 times for mean of 36500 and standard deviation of 5000 miles
## Calculate payoff of $1 per 100 miles that is less than 30000 miles
## Mean of that payoff would be the expected cost of promotion per tire
#

set.seed(105)

sim <- as.integer (rnorm (1000, mean = 36500, sd = 5000))
sim2 = as.integer(rnorm (1000, mean = 40000, sd = 5000))
diff <- as.integer (sim - 30000)
diff2 = as.integer(sim2 - 30000)
payoff <- as.integer (ifelse (diff < 0, (abs (diff) * 0.01), 0))
payoff2 = as.integer(ifelse (diff < 0, (abs (diff2) * .05), 0))
pertire <- mean (payoff)
pertire2 = mean(payoff2)
## Expeccted cost of promotion per tire

print (pertire)
print(pertire2)
morethan50 <- sum (payoff > 50)
more = sum(payoff2 > 50)
probformorethan50 <- morethan50 /1000
prob = more/1000
## Probability of refund more than $50 for a tire

print (probformorethan50)
print(prob)
