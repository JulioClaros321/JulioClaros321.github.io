#Julio Claros

fifa = read.csv(file.choose())
Fifa_Barcelona = subset(fifa, Club == "FC Barcelona")
Fifa_Longford = subset(fifa, Club == "Longford Town")

variables = c("Shot_Power", "Finishing", "Long_Shots", "Curve", "Freekick_Accuraccy", "Shot_Pass", "Long_Pass")
All_Fifa_Players = c(fifa$Shot_Power, fifa$Finishing, fifa$Long_Shots, fifa$Curve, fifa$Freekick_Accuracy, fifa$Short_Pass, fifa$Long_Pass)
summary(All_Fifa_Players)
sd(All_Fifa_Players)
length(fifa$Name)
  
  
Fc_Barcelona = c(Fifa_Barcelona$Shot_Power, Fifa_Barcelona$Finishing, Fifa_Barcelona$Long_Shots, Fifa_Barcelona$Curve, Fifa_Barcelona$Freekick_Accuracy, Fifa_Barcelona$Short_Pass, Fifa_Barcelona$Long_Pass)
summary(Fc_Barcelona)
sd(Fc_Barcelona)
length(Fifa_Barcelona$Name)
  
Longford_Town = c(Fifa_Longford$Shot_Power, Fifa_Longford$Finishing, Fifa_Longford$Long_Shots, Fifa_Longford$Curve, Fifa_Longford$Freekick_Accuracy, Fifa_Longford$Short_Pass, Fifa_Longford$Long_Pass)
summary(Longford_Town)
sd(Longford_Town) 
length(Fifa_Longford$Name)
  
lol = 1.96 * ((18.37)/(sqrt(17588)))
37.71 - (1.96 * ((13.75)/(sqrt(25))))