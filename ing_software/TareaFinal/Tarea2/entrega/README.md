# README.md - Tarea 2: Refactorización y Calidad de Código

## Resumen

Esta entrega corresponde a la Tarea 2 del curso, basada en la refactorización de un sistema de gestión de vuelos para la aerolínea ficticia "GlobalSky Logistics". El sistema original fue reescrito aplicando principios de diseño, pruebas unitarias y análisis con linters.

---

## Estructura del Archivos finales

```
Tarea2_MCD/
├── main_refactorizado.py     # Código refactorizado del sistema de vuelos
├── tests_unitarios.py        # Tests unitarios con unittest
├── .pylintrc                 # Configuración personalizada de pylint
├── P1_REFACTOR.md            # Documento explicando la refactorización
├── P2_TESTING.md             # Documento explicando los tests
├── P3_LINTING.md             # Documento explicando el linter
├── README.md                 # Este archivo
```

---

## Ejecución del script inicial

Para ejecutar el sistema principal:

```bash
python main_refactorizado.py
```

Esto mostrará operaciones básicas del sistema: vuelos, pasajeros, rutas directas y con escalas, entre otras.

---

## Testeo

Para correr los tests unitarios:

```bash
python -m unittest tests_unitarios.py
```

Todos los tests deben pasar exitosamente.

---

## ✅ Verificación de Estilo con Linter

Instalar pylint si no está instalado:

```bash
pip install pylint
```

Ejecutar el linter con la configuración personalizada:

```bash
pylint main.py --rcfile=.pylintrc
```

Esto generará un análisis de estilo, formato y calidad del código fuente.