# install.packages("nlme")
library(nlme)
?BodyWeight
head(BodyWeight)

library(ggplot2)

ggplot(data = BodyWeight, aes(x = Time, y = weight, color = Diet)) +
  geom_point() + geom_smooth(method = "lm") +
  theme_bw() + 
  facet_wrap(~Rat)


library(nlme)
library(ggplot2)
?BodyWeight
head(BodyWeight)

ggplot(data = BodyWeight, aes(x = Time, y = weight, color = Diet)) +
  geom_point() + geom_smooth(method = "lm") +
  theme_bw() + 
  facet_wrap(~Rat)


# Agregando un intercepto aleatorio
# aca el tiempo representa una pendiente y la Dieta es la elevacion de la pendiente
fit <- lme(weight ~ Time + Diet, random = ~ 1|Rat, data = BodyWeight)
summary(fit)



# especificamos que la dieta y el tiempo interactuen entre sí. La dieta va a incidir en la pendiente
# La pendiente global, en este caso del grupo 1, que es 0.35 se ve aumentada en
#  0.6 si pasamos a los ratones de dieta 2.
# Y aumentado en 0.29 si pasamos a los ratones de la dieta 3.
fit <- lme(weight ~ Time * Diet, random = ~ 1|Rat, data = BodyWeight)
summary(fit)



# Intercepto y pendiente aleatoria
fit <- lme(weight ~ Time * Diet, random = ~ 1 + Time|Rat,
           data = BodyWeight)
summary(fit)
