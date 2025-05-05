# Uso de Pylint en Jupyter Notebook

Este documento explica cómo configurar y utilizar Pylint en Jupyter Notebook, incluyendo las diferencias con respecto a su uso en la consola local.

## Instalación

Para usar Pylint en Jupyter Notebook, primero necesitas instalarlo. Puedes hacerlo desde una celda del notebook:

```python
!pip install pylint
```

## Configuración

El archivo `.pylintrc` que ya tienes configurado seguirá funcionando, pero asegúrate de que esté en:
- El directorio raíz de tu proyecto
- El directorio de trabajo actual del notebook

Para una mejor compatibilidad con Jupyter, considera modificar la sección `[REPORTS]` en tu `.pylintrc`:

```ini
[REPORTS]
output-format=text  # En lugar de colorized
```

## Métodos de Ejecución

### 1. Usando el comando mágico `%%pylint`

```python
%%pylint
# Tu código aquí
```

### 2. Usando el comando `!pylint`

```python
!pylint tu_archivo.py
```

### 3. Especificando el archivo de configuración

```python
!pylint --rcfile=.pylintrc tu_archivo.py
```

## Diferencias con la Consola Local

1. **Salida**: 
   - Los resultados se muestran en la celda del notebook
   - El formato puede verse ligeramente diferente

2. **Comandos**:
   - Necesitas usar el prefijo `!` o `%%` para comandos del sistema
   - Ejemplo: `!pylint` en lugar de `pylint`

3. **Rutas**:
   - El directorio de trabajo puede ser diferente
   - Asegúrate de que las rutas sean correctas

4. **Formato**:
   - Los colores pueden verse diferentes o no mostrarse
   - Algunas opciones de formato pueden necesitar ajustes

## Consejos Adicionales

1. **Análisis de Celdas Específicas**:
   - Usa `%%pylint` al inicio de la celda que quieres analizar

2. **Análisis de Archivos Completos**:
   - Usa `!pylint --rcfile=.pylintrc ruta/al/archivo.py`

3. **Configuración Personalizada**:
   - Puedes crear diferentes archivos `.pylintrc` para diferentes proyectos
   - Especifica el archivo de configuración usando `--rcfile`

## Solución de Problemas

Si encuentras problemas:
1. Verifica que Pylint esté instalado correctamente
2. Asegúrate de que el archivo `.pylintrc` esté en la ubicación correcta
3. Comprueba que las rutas a los archivos sean correctas
4. Si los colores no se muestran correctamente, cambia `output-format` a `text`

## Ejemplo Completo

```python
# Instalación
!pip install pylint

# Análisis de un archivo específico
!pylint --rcfile=.pylintrc mi_archivo.py

# Análisis de código en una celda
%%pylint
def mi_funcion():
    x = 1
    return x
``` 