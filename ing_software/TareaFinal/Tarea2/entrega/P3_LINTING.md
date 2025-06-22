# LINTING.md - Verificación de Estilo con Pylint

## Objetivo

Configurar y ejecutar un linter para asegurar que el código cumpla con buenas prácticas de estilo y diseño.

---

## Herramienta Utilizada

Se utilizó `pylint` para analizar el código Python del sistema de vuelos.

Instalación:

```bash
pip install pylint
```

---

## Configuración (`.pylintrc`)

Se configuró `pylint` para:

* Verificar al menos **10 errores comunes**.
* Excluir la verificación `missing-docstring` como parte del requerimiento de exclusión.
* Limitar la longitud máxima de línea a 100 caracteres.

Principales reglas configuradas:

| Tipo de Error          | Descripción                                                  |
| ---------------------- | ------------------------------------------------------------ |
| `unused-import`        | Importaciones no utilizadas                                  |
| `unused-variable`      | Variables no utilizadas                                      |
| `redefined-outer-name` | Nombres redefinidos que pueden generar ambigüedad            |
| `too-many-arguments`   | Funciones con demasiados argumentos                          |
| `too-many-branches`    | Funciones con demasiadas bifurcaciones                       |
| `too-many-statements`  | Funciones con demasiadas instrucciones                       |
| `too-many-locals`      | Uso excesivo de variables locales                            |
| `line-too-long`        | Líneas que exceden el límite establecido (100)               |
| `invalid-name`         | Nombres de variables o funciones no descriptivos             |
| `no-member`            | Acceso a atributos que no existen (verificado estáticamente) |

Regla excluida:

* `missing-docstring`: omisión de docstrings.

---

## Ejecución del Linter

```bash
pylint main.py --rcfile=.pylintrc
```

---

## Procesamiento de Salida (Opcional)

Se puede redirigir la salida a un archivo:

```bash
pylint main_factorizado.py --rcfile=.pylintrc > reporte_linter.txt
```

Y analizarla manualmente o con un script.

---

## Resultado Esperado

El sistema debe obtener un puntaje positivo y legible. Se espera que las reglas configuradas ayuden a mantener el estilo limpio y consistente.

---