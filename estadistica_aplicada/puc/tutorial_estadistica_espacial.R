# install.packages("spdep")
library(spdep)
library(rio)

#Source: https://github.com/mgimond

df <- import("nhme.RData")

# DistribuciÃ³n espacial ---------------------------------------------------

plot(df)
plot(df["Income"])
plot(df["Income"], breaks = "quantile", nbreaks = 4)

nb <- poly2nb(df)
lw <- nb2listw(nb, zero.policy = TRUE)

# Test de moran -----------------------------------------------------------

moran.test(df$Income, lw)





# Segundo Tutorial

library(sp)
library(gstat)

data(meuse)
head(meuse)
coordinates(meuse) <- ~ x + y

# Variograma empirico -----------------------------------------------------

v <- variogram(log(zinc) ~ 1, data = meuse) # explicado a nivel global
plot(v)

# Ajuste de modelo --------------------------------------------------------

fit <- fit.variogram(v, model = vgm("Mat"))
plot(v, model = fit)

# Prediccion --------------------------------------------------------------

newdata <- data.frame(x = 178000, y = 329714)
coordinates(newdata) <- ~ x + y
krige(log(zinc) ~ 1, meuse, newdata, model = fit)


newdata
