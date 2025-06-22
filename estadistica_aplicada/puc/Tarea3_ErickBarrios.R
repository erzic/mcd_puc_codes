getwd()

library(sp)
library(gstat)
library(ggplot2)
library(kriging)

# Leyendo Datos
data <- read.table("RealEstate.txt",sep=" ", header = TRUE)
data_og <- read.table("RealEstate.txt",sep=" ", header = TRUE)
head(data)

get_mode <- function(x) {
  uniq_x <- unique(x)
  uniq_x[which.max(tabulate(match(x, uniq_x)))]
}

# Pregunta 1
hist(data$logSellingPr, col="darkblue", main = "Logaritmo Precio de Venta", breaks = 16, xlab="")
summary(data$logSellingPr)
get_mode(data$logSellingPr)

conteo.precios <- table(data$logSellingPr)
barplot(conteo.precios, main = "Precio", col="darkblue")


# Pregunta 2
ggplot(data, aes(x=logSellingPr, y=LivingArea)) + geom_point() + ggtitle("Precio vs Superficie sala de estar")
ggplot(data, aes(x=logSellingPr, y=Age)) + geom_point() + ggtitle("Precio vs Antigüedad")
ggplot(data, aes(x=logSellingPr, y=OtherArea)) + geom_point() + ggtitle("Precio vs Otras Áreas")
ggplot(data, aes(x=Bedrooms,y=logSellingPr, group=Bedrooms)) + geom_boxplot() + ggtitle("Precio vs Habitaciones")
ggplot(data, aes(x=Bathrooms,y=logSellingPr, group=Bathrooms)) + geom_boxplot() + ggtitle("Precio vs Baños")
ggplot(data, aes(x=HalfBaths,y=logSellingPr, group=HalfBaths)) + geom_boxplot() + ggtitle("Precio vs Medios Baños")

# Pregunta 3

coordinates(data)<-~Latitude+Longitude

# Pregunta 4
v <- variogram(logSellingPr ~ 1, data = data) # explicado a nivel global
plot(v, col='darkblue')


# Pregunta 5
fit_esferico <- fit.variogram(v, model = vgm(psill = 0.09,model = "Sph",range = 0.15, nugget=0.03))
plot(v, model = fit_esferico, main="Ajustando Modelo Esférico")

fit_exponencial <- fit.variogram(v, model = vgm(psill = 0.08,model = "Exp", nugget=0.06), fit.range=F)
plot(v, model = fit_exponencial, main="Ajustando Modelo Exponencial")


# Pregunta 6
pred_sph <- kriging(data_og$Longitude,data_og$Latitude, data_og$logSellingPr, model = "spherical")
pred_exp <- kriging(data_og$Longitude,data_og$Latitude, data_og$logSellingPr, model = "exponential")

newdata <- data.frame(x = c(-90, -95), y = c(30, 33))
coordinates(newdata) <- ~ x + y

krige(logSellingPr~1, locations = data, newdata = newdata, model =fit_esferico)
krige(logSellingPr~1, locations = data, newdata = newdata, model =fit_exponencial)



# Pregunta 8
library(ks)
library(ggplot2)


coords <- as.matrix(data_og[, c("Longitude", "Latitude")])
weights <- data_og$logSellingPr


kde_result <- kde(x = coords, w = weights, gridsize = c(100, 100))


dens_df <- expand.grid(
  Longitude = kde_result$eval.points[[1]],
  Latitude = kde_result$eval.points[[2]]
)
dens_df$Density <- as.vector(kde_result$estimate)


ggplot(dens_df, aes(x = Longitude, y = Latitude, fill = Density)) +
  geom_raster(interpolate = TRUE) +
  scale_fill_viridis_c() +
  theme_minimal() +
  labs(
    title = "Mapa de Calor ponderado por el Precio",
    x = "Longitud",
    y = "Latitud",
    fill = "Precio"
  )

