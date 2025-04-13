# Introduccion ------------------------------------------------------------

install.packages("survival")
library(survival)
library(dplyr)
?veteran

veteran %>% head

# Objeto Survival -------------------------------------------------------

Surv(veteran$time, veteran$status)
#Status 1 : tiempo de falla
#Status 0: tiempo de censura

# Kaplan-Meier ------------------------------------------------------------

fit1 <- survfit(Surv(time, status) ~ 1, data = veteran)
plot(fit1)

fit2 <- survfit(Surv(time, status) ~ trt, data = veteran)
plot(fit2, col = c("red", "blue"))
legend("topright", c("trt = 1", "trt = 2"),
       col = c("red", "blue"), lty = c(1, 1))

# ggplot2 -----------------------------------------------------------------

install.packages("survminer")
library(survminer)
?ggsurvplot

ggsurvplot(fit1)
ggsurvplot(fit2)




# Log Rank Test ------------------------------------------------------------

# install.packages("survival")
library(survival)
?veteran

head(veteran)

# Log rank test -----------------------------------------------------------

survdiff(Surv(time, status) ~ trt, data = veteran)

# ggplot2 -----------------------------------------------------------------

library(survminer)

fit <- survfit(Surv(time, status) ~ trt, data = veteran)

ggsurvplot(fit, pval = TRUE) 
