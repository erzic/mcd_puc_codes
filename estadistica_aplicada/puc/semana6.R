library(nlme)
library(ggplot2)

ggplot(data = BodyWeight, aes(x = Time, y = weight, color = Diet)) +
  geom_point() + geom_smooth(method = "lm") +
  theme_bw() + 
  facet_wrap(~Rat)

# lme(weight ~ Time * Diet, random = ~ 1|Rat, data = BodyWeight)

fit <- lme(weight ~ Time * Diet, random = ~ Time|Rat,
           data = BodyWeight)
summary(fit)
