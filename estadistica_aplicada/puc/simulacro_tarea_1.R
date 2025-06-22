library(survival)
library(survminer)
library(ggfortify) 
library(ggplot2)
library(tidyverse)

### Datos sobre un ensayo aleatorizado de dos regímenes de
##  tratamiento para el cáncer de pulmón en veteranos de guerra.
head(veteran)
?veteran ## acceder a la descripción de cada variable

## Ejemplos de análisis descriptivo de algunas variables.
table1 <- table(veteran$celltype) %>% prop.table() %>% round(2) %>% as.data.frame()

ggplot(table1, aes(x = "", y = Freq, fill = Var1)) +
  geom_bar(width = 1, stat = "identity") +
  coord_polar("y", start = 0) +
  geom_text(aes(label = Freq),
            position = position_stack(vjust = 0.5)) +
  scale_fill_brewer("", palette="Blues") +
  ggtitle("Celltype ")+
  theme_minimal()

ggplot(veteran, aes(x = age)) + 
  geom_boxplot(outlier.colour = "black",
               outlier.shape = 16,
               outlier.size = 2,
               notch = FALSE) +
  theme_minimal() + ggtitle("age")



## Kaplan-Meier
fit <- survfit(Surv(time,status) ~ trt, data = veteran)
fit

# Gráfica de la función de supervivencia y mediana de supervivencia
ggsurvplot(fit, data = veteran, 
           conf.int = TRUE, 
           conf.int.style = "step", 
           surv.median.line = "hv", 
           pval = TRUE)

survdiff(Surv(time,status) ~ trt, data = veteran)

fit2 <- survfit(Surv(time,status) ~ celltype, data = veteran)
fit2

ggsurvplot(fit2, data = veteran, 
           conf.int = FALSE, 
           surv.median.line = "hv", 
           pval = TRUE)
survdiff(Surv(time,status) ~ celltype, data = veteran)




# Ajuste del modelo
## Ejercicio de interpretación de los coeficientes
model <- coxph(Surv(time, status) ~ trt, data = veteran)
summary(model)

## Ajustamos el modelo con varias variables de la data
modelfull <- coxph(Surv(time, status) ~ trt + celltype + karno + age, data = veteran)
summary(modelfull)

## Seleccionamos aquellas variables significativas resultantes del ajuste anterior
modelselected <- coxph(Surv(time, status) ~ celltype + karno, data = veteran)
summary(modelselected)