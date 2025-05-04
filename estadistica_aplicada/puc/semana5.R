library(nlme)
library(ggplot2)
head(BodyWeight)

ggplot(data=BodyWeight, aes(x=Time, y=weight, color=Diet)) +
  geom_point() + geom_smooth(method="lm")+
  theme_bw() +
  facet_wrap(~ Rat)

# Ajustando modelos mixtos
# random = ~ 1 especifica que estamos metiendo un intercepto aleatorio
fit <- lme(weight ~ Time + Diet, random = ~ 1|Rat, data=BodyWeight)
summary(fit)

fit <- lme(weight ~ Time*Diet, random = ~ 1|Rat, data=BodyWeight)
summary(fit)
