comparison = table(gss$SEX, gss$useSocialMedia)
barplot(comparison, main = "Variations of Social Media User by Sex", 
        xlab="Types of Social Media Websites", col=c("Blue", "Red"), ylab="Number of Users", names=c("lol")