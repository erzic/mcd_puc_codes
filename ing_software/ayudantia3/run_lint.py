#!/usr/bin/env python3
"""
Script para ejecutar pylint y mostrar los resultados de manera amigable.
"""
import subprocess
import sys
import os
import re
from typing import List, Dict

# Diccionario con las descripciones en español de los códigos de error
ERROR_DESCRIPTIONS: Dict[str, str] = {
    # Errores de convención (C)
    "C0301": "Línea demasiado larga",
    "C0303": "Espacios en blanco al final de la línea",
    "C0304": "Falta nueva línea al final del archivo",
    "C0305": "Demasiadas líneas en blanco al final",
    "C0321": "Múltiples declaraciones en una línea",
    "C0410": "Múltiples imports en una línea",
    "C2401": "Nombre de función contiene caracteres no ASCII",
    
    # Errores (E)
    "E0102": "Función ya definida",
    
    # Advertencias (W)
    "W0301": "Punto y coma innecesario",
    "W0311": "Indentación incorrecta",
    "W0602": "Uso de variable global sin asignación",
    "W0603": "Uso de la declaración global",
    "W0612": "Variable no utilizada",
    "W0702": "Excepción sin tipo especificado",
    "W4701": "Lista iterada modificada dentro del bucle",
}

def get_error_description(code: str) -> str:
    """Obtiene la descripción en español de un código de error."""
    # Eliminar los dos puntos si existen
    code = code.rstrip(':')
    return ERROR_DESCRIPTIONS.get(code, f"Código desconocido: {code}")

def run_pylint(files: List[str]) -> None:
    """Ejecuta pylint en los archivos especificados."""
    print("🔍 Ejecutando pylint...\n")
    
    # Buscar pylint
    pylint_path = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Python", f"Python{sys.version_info.major}{sys.version_info.minor}", "Scripts", "pylint.exe")
    
    if not os.path.exists(pylint_path):
        print("❌ No se encontró pylint. Por favor, instálalo con:")
        print("pip install pylint")
        sys.exit(1)
    
    print(f"✅ pylint encontrado en: {pylint_path}\n")
    
    # Construir el comando
    cmd = [pylint_path] + files
    
    try:
        # Ejecutar pylint
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        # Mostrar resultados
        if result.returncode == 0:
            print("✅ No se encontraron problemas de estilo")
        else:
            print("⚠️ Se encontraron los siguientes problemas:\n")
            print(result.stdout)
            
            # Contar errores y advertencias usando expresiones regulares
            error_pattern = r'[A-Z]\d{4}(?=:)'
            errors = re.findall(error_pattern, result.stdout)
            
            # Clasificar por tipo de problema
            error_codes = set(errors)
            error_counts = {code: errors.count(code) for code in error_codes}
            
            print("\n📊 Resumen detallado:")
            for code, count in sorted(error_counts.items()):
                description = get_error_description(code)
                print(f"  - {code}: {description} ({count} ocurrencias)")
            
            total_errors = len(errors)
            print(f"\n📊 Resumen total:")
            print(f"  - Total de problemas: {total_errors}")
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al ejecutar pylint: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Archivos a analizar
    files_to_check = ["api.py", "classes.py", "test.py", "main_sucio.py"]
    run_pylint(files_to_check) 