library(sp)
library(gstat)

data(meuse)
?meuse
str(meuse)

meuse$zinc

hist(meuse$zinc, col="darkblue", main = "Zinc", breaks = 16, xlab="")

summary(meuse$zinc)

conteo.soil <- table(meuse$soil)
barplot(conteo.soil, main = "Soil", col="darkblue")


meuse$logZn <- log10(meuse$zinc)

hist(meuse$logZn , col="darkblue", main = "Log10 Zinc", xlab="")
summary(meuse$logZn)

coordinates(meuse) <- c("x","y")
class(meuse)
plot(meuse, asp = 1, pch = 1)

data(meuse.riv)
lines(meuse.riv)


n <- length(meuse$logZn)
n*(n-1)/2

coordinates(meuse)[1,]
coordinates(meuse)[2,]

sep <- dist(coordinates(meuse)[1:2,])
sep
## semivarianza
gamma <- 0.5*(meuse$logZn[1]-meuse$logZn[2])^2
gamma






## Variograma empírico
ve <- variogram(logZn~1, meuse, cutoff=1300, width = 90)
ve
plot(ve)

## Ajuste visual

fit.sph <- fit.variogram(ve, model = vgm(psill = 0.12,model = "Sph", 
                                         range = 850, nugget = 0.01))
plot(ve, model=fit.sph)


## Ajuste automático
vt <- vgm(psill = 0.12,model = "Sph", 
          range = 850, nugget = 0.01)
va <- fit.variogram(ve, vt)
plot(ve, pl = T, model = va)
## Kriging ordinario

data(meuse.grid)
coordinates(meuse.grid) <- c("x","y")
gridded(meuse.grid) <- T

ok <- krige(logZn~1, locations = meuse, newdata = meuse.grid, model =fit.sph)
ok$pred <- 10^(ok$var1.pred)
str(ok)
head(ok)


## una coordenada

newdata <- data.frame(x = 500, y = 890)
coordinates(newdata) <- ~ x + y

krige(logZn~1, locations = meuse, newdata, model = fit.sph)


