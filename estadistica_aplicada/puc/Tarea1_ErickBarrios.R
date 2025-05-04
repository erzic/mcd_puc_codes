# librerias
library(survival)
library(survminer)
library(ggfortify) 
library(ggplot2)
library(tidyverse)


# Pregunta 1 - Analisis exploratorio
# variable objetivo: week (tiempo) , arres (flag de si fue arrastrado)

#data <- read_table(file="Rossi.txt")
data <- read.csv(file="Rossi.txt",header = TRUE,sep = ' ')

summary(data)

ggplot(data=data, aes(y=fin, x=week, group = fin)) +
  geom_boxplot() +
  geom_jitter(color="black", size=0.4, alpha=0.9) +
  ggtitle("Variable: Recibe Ayuda Economica")
  
ggplot(data=data, aes(y=race, x=week, group = race)) +
  geom_boxplot() +
  geom_jitter(color="black", size=0.4, alpha=0.9) +
  ggtitle("Variable: Raza")

ggplot(data=data, aes(y=wexp, x=week, group = wexp)) +
  geom_boxplot() +
  geom_jitter(color="black", size=0.4, alpha=0.9) +
  ggtitle("Variable: Experiencia Laboral")

ggplot(data=data, aes(y=mar, x=week, group = mar)) +
  geom_boxplot() +
  geom_jitter(color="black", size=0.4, alpha=0.9) +
  ggtitle("Variable: Estado Civil")


ggplot(data=data, aes(y=paro, x=week, group = paro)) +
  geom_boxplot() +
  geom_jitter(color="black", size=0.4, alpha=0.9) +
  ggtitle("Variable: Libertad Condicional")

# ggplot(data, aes(x = prio, y = week)) +
#   geom_point() +
#   labs(title = "Condenas anteriores vs Tiempo de Reincidencia",
#        x = "Condenas anteriores",
#        y = "Tiempo de Reincidencia")
# 
# ggplot(data, aes(x = educ, y = week)) +
#   geom_point() +
#   labs(title = "Nivel educativo vs Tiempo de Reincidencia",
#        x = "Nivel Educativo",
#        y = "Tiempo de Reincidencia")


ggplot(data=data, aes(x=prio, y=arrest, group = arrest)) +
  geom_boxplot() +
  geom_jitter(color="black", size=0.4, alpha=0.9) +
  ggtitle("Variable: Condenas Anteriores")

ggplot(data=data, aes(x=educ, y=arrest, group = arrest)) +
  geom_boxplot() +
  geom_jitter(color="black", size=0.4, alpha=0.9) +
  ggtitle("Variable: Nivel Educativo")

# Pregunta 2: Test de Log Rank


fit_fin = survfit(Surv(week, arrest) ~ fin, data = data)
ggsurvplot(fit_fin, data = data, 
           conf.int = TRUE, 
           conf.int.style = "step", 
           surv.median.line = "hv", 
           pval = TRUE) + ggtitle("Curvas para variable fin")

fit_race = survfit(Surv(week, arrest) ~ race, data = data)
ggsurvplot(fit_race, data = data, 
           conf.int = TRUE, 
           conf.int.style = "step", 
           surv.median.line = "hv", 
           pval = TRUE) + ggtitle("Curvas para variable race")

fit_wexp = survfit(Surv(week, arrest) ~ wexp, data = data)
ggsurvplot(fit_wexp, data = data, 
           conf.int = TRUE, 
           conf.int.style = "step", 
           surv.median.line = "hv", 
           pval = TRUE) + ggtitle("Curvas para variable wexp")

fit_mar = survfit(Surv(week, arrest) ~ mar, data = data)
ggsurvplot(fit_mar, data = data, 
           conf.int = TRUE, 
           conf.int.style = "step", 
           surv.median.line = "hv", 
           pval = TRUE) + ggtitle("Curvas para variable mar")

fit_paro = survfit(Surv(week, arrest) ~ paro, data = data)
ggsurvplot(fit_paro, data = data, 
           conf.int = TRUE, 
           conf.int.style = "step", 
           surv.median.line = "hv", 
           pval = TRUE) + ggtitle("Curvas para variable paro")

fit_prio = survfit(Surv(week, arrest) ~ prio, data = data)
ggsurvplot(fit_prio, data = data, 
           conf.int = TRUE, 
           conf.int.style = "step", 
           surv.median.line = "hv", 
           pval = TRUE) + ggtitle("Curvas para variable prio")


fit_educ = survfit(Surv(week, arrest) ~ educ, data = data)
ggsurvplot(fit_educ, data = data, 
           conf.int = TRUE, 
           conf.int.style = "step", 
           surv.median.line = "hv", 
           pval = TRUE) + ggtitle("Curvas para variable educ")

survdiff(Surv(week, arrest) ~ fin, data = data)
survdiff(Surv(week, arrest) ~ race, data = data)
survdiff(Surv(week, arrest) ~ wexp, data = data)
survdiff(Surv(week, arrest) ~ mar, data = data)
survdiff(Surv(week, arrest) ~ paro, data = data)
survdiff(Surv(week, arrest) ~ prio, data = data)
survdiff(Surv(week, arrest) ~ educ, data = data)

survdiff(Surv(week, arrest) ~ fin+wexp+mar+educ, data = data)

# Pregunta 3
fit_completo <- coxph(Surv(week, arrest) ~ fin + race + wexp + mar + paro + prio + educ, data = data)
summary(fit_completo)

# Pregunta 4 y 5
fit_sign <- coxph(Surv(week, arrest) ~ fin + prio , data = data)
summary(fit_sign)
# tener aporo financiero reduce el riesgo de ser arrestado
# tener más condenas es un factor de riesgo, es decir, las personas con más condenas anteriores tiene mayor probabilidad de ser arrestado de nuevo

# Pregunta 6  

ftest <- cox.zph(fit_sign)
ftest
# No se rechaza la H0 de que los riesgos son proporcionales

