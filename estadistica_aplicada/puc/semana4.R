# IntroducciÃ³n ------------------------------------------------------------

# install.packages("survival")
library(survival)
?veteran

# Modelo de Cox -----------------------------------------------------------

fit1 <- coxph(Surv(time, status) ~ trt, data = veteran)
fit1

summary(fit1)

fit2 <- coxph(Surv(time, status) ~ trt + celltype, data = veteran)
fit2

summary(fit2)


# Introduccion ------------------------------------------------------------

# install.packages("survival")
library(survival)
?veteran

veteran %>% head

# Modelo de Cox -----------------------------------------------------------

fit1 <- coxph(Surv(time, status) ~ trt, data = veteran)
fit1

fit2 <- coxph(Surv(time, status) ~ trt + celltype, data = veteran)
fit2

# Riesgos proporcionales --------------------------------------------------

cox.zph(fit1)
cox.zph(fit2)

# ggplot2 -----------------------------------------------------------------

library(survminer)

fit3 <- survfit(Surv(time, status) ~ trt, data = veteran)
ggsurvplot(fit3, fun = "cloglog")




