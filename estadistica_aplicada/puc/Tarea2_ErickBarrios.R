library(nlme)
library(ggplot2)
?Orthodont
datos <- Orthodont
head(datos)

# Pregunta 1: Analisis exploratorio

boxplots_sex <- ggplot(data = datos, mapping = aes(x=Sex, y=distance))
boxplots_sex + geom_boxplot(aes(colour = Sex)) + geom_jitter(width = 0.05) + ggtitle("Distribución por Sexo")

histogramas_sex <- ggplot(datos, aes(x=distance, color=Sex))
histogramas_sex + geom_histogram(binwidth = 0.5)

ggplot(data = datos, aes(x = age, y = distance, color = Sex)) +
  geom_point() + geom_smooth(method = "lm") +
  theme_bw() + 
  facet_wrap(~Subject)

ggplot(data = datos, aes(x = age, y = distance, color = Sex)) +
  geom_point() + geom_smooth(method = "lm") +
  theme_bw()


# Pregunta 2

# Modelo Mixto con Intercepto Aleatorio
modelo_intercepto <- lme(distance ~ age, random=~1|Subject, data = datos)
summary(modelo_intercepto)

# Modelo Mixto con Intercepto y Pendiente Aleatoria
modelo_intercepto_pendiente <- lme(distance ~ age, random=~ 1 + age|Subject, data = datos)
summary(modelo_intercepto_pendiente)


# Pregunta 4

datos$es_varon <- ifelse(datos$Sex=="Male", 1, 0)
modelo_custom <- lm(distance ~ age, data = datos)
summary(modelo_custom)

modelo_custom <- lm(distance ~ age + Sex, data = datos)
summary(modelo_custom)

modelo_custom_mixto <- lme(distance ~ age + Sex, random=~ 1 + age + Sex|Subject, data = datos)
summary(modelo_custom_mixto)

# Analisis por Separado
varones <- datos[datos$Sex=="Male", ]
mujeres <- datos[datos$Sex=="Female", ]

# Modelo Mixto con Intercepto Aleatorio
modelo_intercepto <- lme(distance ~ age, random=~1|Subject, data = varones)
summary(modelo_intercepto)

# Modelo Mixto con Intercepto y Pendiente Aleatoria
modelo_intercepto_pendiente <- lme(distance ~ age, random=~ 1 + age|Subject, data = varones)
summary(modelo_intercepto_pendiente)


# Modelo Mixto con Intercepto Aleatorio
modelo_intercepto <- lme(distance ~ age, random=~1|Subject, data = mujeres)
summary(modelo_intercepto)

# Modelo Mixto con Intercepto y Pendiente Aleatoria
modelo_intercepto_pendiente <- lme(distance ~ age, random=~ 1 + age|Subject, data = mujeres)
summary(modelo_intercepto_pendiente)

getwd()
