# TESTING.md - Tests Unitarios para el Sistema de Vuelos

## Objetivo

Implementar una batería de tests unitarios que verifiquen el funcionamiento correcto del sistema de vuelos tras su refactorización.

---

## Descripción

El archivo `test_main.py` incluye 10 pruebas unitarias usando `unittest`, cubriendo las siguientes funcionalidades:

### 1. Agregar Vuelos

* Verifica que los vuelos se agreguen correctamente al sistema.

### 2. Eliminar Vuelos

* Verifica que los vuelos se eliminen correctamente y se borren los pasajeros asociados.

### 3. Búsqueda de Vuelos Directos

* Verifica que se encuentre un vuelo directo dado origen y destino.

### 4. Búsqueda con Escalas

* Verifica que se encuentren rutas posibles con una escala.

### 5. Visualización de Pasajeros

* Verifica que la lista de pasajeros sea precisa por vuelo.

### 6. Descenso Total de Pasajeros

* Verifica que todos los pasajeros de un vuelo se eliminen correctamente.

### 7. Descenso Parcial de Pasajeros

* Verifica que solo una parte de los pasajeros baje del vuelo.

### 8. Consulta de Hora de Vuelo

* Verifica que la hora asignada al vuelo sea la esperada.

### 9. Verificar Persistencia de Lista de Pasajeros

* Verifica que el resto de pasajeros permanezcan tras una baja parcial.

### 10. Confirmar Existencia de Conexiones

* Verifica que existan rutas indirectas entre ciudades conectadas.

---

## Ejecución de los Tests

Desde el cmd, posicionados en la carpeta conteniendo el archivo con los tests, ejecutar:

```bash
python -m unittest tests_unitarios.py
```

Todos los tests deben pasar correctamente sin errores.

---

## Recomendaciones

* Ejecutar los tests automáticamente tras modificaciones del sistema.
* Incluir nuevos tests al agregar funcionalidades.
* Mantener los tests independientes y repetibles.

---