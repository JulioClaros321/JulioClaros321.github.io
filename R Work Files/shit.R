chart = load(file.choose())
library(car)
gss$tw <- recode(as.integer(gss$TWITTER), " 1=1; 2=0 ")
gss$fb <- recode(as.integer(gss$FACEBOOK), " 1=1; 2=0 ")
gss$ig <- recode(as.integer(gss$INSTAGRM), " 1=1; 2=0 ")
gss$li <- recode(as.integer(gss$LINKEDIN), " 1=1; 2=0 ")
gss$sn <- recode(as.integer(gss$SNAPCHAT), " 1=1; 2=0 ")
gss$tu <- recode(as.integer(gss$TUMBLR), " 1=1; 2=0 ")
gss$wh <- recode(as.integer(gss$WHATSAPP), " 1=1; 2=0 ")
gss$go <- recode(as.integer(gss$GOOGLESN), " 1=1; 2=0 ")
gss$pi <- recode(as.integer(gss$PINTERST), " 1=1; 2=0 ")
gss$fl <- recode(as.integer(gss$FLICKR), " 1=1; 2=0 ")
gss$vi <- recode(as.integer(gss$VINE), " 1=1; 2=0 ")
gss$cl <- recode(as.integer(gss$CLSSMTES), " 1=1; 2=0 ")

# combine into a single ratio scale variable
gss$useSocialMedia <- gss$tw + gss$fb + gss$ig + gss$li + gss$sn + gss$tu +
  gss$wh + gss$go + gss$pi + gss$fl + gss$vi + gss$cl

# remove recoded helper variables
gss[, c("tw","fb","ig","li","sn","tu","wh","go","pi","fl","vi","cl")] <- NULL

summary(gss$useSocialMedia)
boxplot(gss$useSocialMedia, xlab = "test", ylab = "test") 
length(which(gss$useSocialMedia > 8))
hist(gss$useSocialMedia)
table(gss$useSocialMedia.integer)

comparison = table(gss$SEX, gss$useSocialMedia)
barplot(comparison, main = "Variations of Social Media User by Sex", 
        xlab="Types of Social Media Websites", col=c("Blue", "Pink"), ylab="Number of Users", )