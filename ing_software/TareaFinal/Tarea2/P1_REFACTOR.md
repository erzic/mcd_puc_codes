# REFACTOR.md - Explicación de Refactorización

## Objetivo

Refactorizar el archivo `main.py` original para mejorar la calidad del código aplicando principios de diseño como SOLID, Clean Code, ocultamiento de información, y eliminación de code smells.

---

## Principales Problemas Detectados

### 1. Variables Globales

* **Problema:** Uso de `flights`, `pasajeros`, `tmp`, `x`, y `debug` como variables globales.
* **Solución:** Encapsulación dentro de la clase `FlightManager`.
* **Principio:** Ocultamiento de información, Responsabilidad Única.

### 2. Nombres Poco Descriptivos

* **Problema:** Uso de nombres como `x`, `f`, `tmp`, `quitar()`.
* **Solución:** Renombrado de variables y funciones por nombres claros y descriptivos (`remove_flight`, `fid`, `show_passengers`).
* **Principio:** Integridad conceptual.

### 3. Ausencia de Orientación a Objetos

* **Problema:** Código puramente procedimental, sin clases.
* **Solución:** Implementación de clases `Flight` y `FlightManager`.
* **Principio:** SOLID (Single Responsibility, Encapsulation, Composition over inheritance).

### 4. Código Repetido y Poco Cohesionado

* **Problema:** Repetición de patrones de búsqueda y modificación en funciones.
* **Solución:** Consolidación de lógica común en métodos con responsabilidad clara.
* **Principio:** Cohesión, Eliminación de *Code Smells* (duplicated code).

### 5. Estilo de Código

* **Problema:** Múltiples instrucciones por línea, uso incorrecto de `exec`, mal formato PEP8.
* **Solución:** Correcciones PEP8, eliminación de `exec`, ordenamiento de imports y estructuras.
* **Principio:** Claridad, mantenibilidad, cumplimiento de PEP8.

---

## Cambios Aplicados

| Problema Original                      | Sección Afectada       | Cambio Realizado                     | Principio Abordado |
| -------------------------------------- | ---------------------- | ------------------------------------ | ------------------ |
| Variables globales                     | Todo el archivo        | Encapsulado en clase                 | Encapsulamiento    |
| Nombres no descriptivos                | `x`, `tmp`, `quitar()` | Nombres descriptivos                 | Claridad           |
| Procedural code                        | Todas las funciones    | Clases y métodos                     | SRP, OOP           |
| Funciones con muchas responsabilidades | `main()`               | Dividido en funciones/métodos        | SRP                |
| Código retutilizado o duplicado        | búsqueda de vuelos     | Consolidado en métodos reutilizables | DRY                |
| No hay un estándar de estilo           | Todas las funciones    | PEP8, comentarios, orden             | Estándares         |


---

## Instrucciones de Ejecución

1. Abrir una CMD en la localización del archivo python. Por ejemplo, si el archivo está en la carpeta 2 dentro de la carpeta 1 en el disco C, se puede correr el siguiente comando:

```bash
cd C:/carpeta1/carpeta2
```

2. Correr el archivo de python de la siguiente manera:

```bash
python main.py
```

Si no funciona, probar las siguientes opciones:

```bash
python3 main.py
```

```bash
py main.py
```

3. Se mostrará salida en consola con pruebas de vuelos, búsquedas y manipulación de pasajeros.

---
