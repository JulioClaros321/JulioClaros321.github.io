week_days = c("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
history_per= c(7, 4, 5, 12, 11, 37, 24)
frequency = c(47, 15, 27, 45, 44, 166, 150)
orders = data.frame(week_days, history_per, frequency)

sum(frequency)
(orders.prop = history_per/100)

chisq.test(x=frequency, p=orders.prop)

candy.color = c("blue", "orange", "green", "red", "yellow", "brown")
candy.obs = c(212, 147, 103, 50, 46, 42)
sum(candy.obs)
(candy.prop2= candy.obs/(sum(candy.obs)))
(candy.prop = c(1/6, 1/6, 1/6, 1/6, 1/6, 1/6))
chisq.test(x=candy.obs, p=candy.prop)