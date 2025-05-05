# test_metro.py
"""
Suite de tests completamente genérica para cualquier implementación de metro.
Sólo asume la existencia de un módulo 'metro' con la siguiente API:

    reset_state()
    add_passenger(name: str, destination: str)
    remove_passenger(name: str, at_station: str)
    move_train()
    get_state() -> {"position": str, "passengers": List[str]}

"""
import sys
import io
import api as metro

def capture_stdout(func):
    buf = io.StringIO()
    old = sys.stdout
    sys.stdout = buf
    try:
        func()
    finally:
        sys.stdout = old
    return buf.getvalue()


def test_add_and_move():
    metro.reset_state()
    metro.add_passenger("Ana", "A")
    metro.add_passenger("Luis", "C")
    state = metro.get_state()
    assert "Ana" in state["passengers"], "Ana debería estar a bordo"
    assert "Luis" in state["passengers"], "Luis debería estar a bordo"

    # Movemos dos veces: A → B, B → C (Luis baja)
    metro.move_train()
    metro.move_train()
    state = metro.get_state()
    assert state["position"] == "C", "El tren debe quedar en C"
    assert "Luis" not in state["passengers"], "Luis debería haberse bajado"


def test_remove_passenger():
    metro.reset_state()
    metro.add_passenger("Carlos", "D")
    assert "Carlos" in metro.get_state()["passengers"], "Carlos debería estar a bordo"
    metro.remove_passenger("Carlos", "D")
    assert "Carlos" not in metro.get_state()["passengers"], "Carlos debe haber sido removido"


def test_status_output():
    metro.reset_state()
    metro.add_passenger("Marta", "B")
    # Capturamos la salida de move_train o status (depende de implementación)
    out = capture_stdout(metro.move_train)
    # Debe mencionar a Marta y la estación B
    assert "Marta" in out, "Debe mencionarse 'Marta' en la salida"
    assert "B" in out, "Debe mencionarse 'B' en la salida"


def test_invalid_destination():
    metro.reset_state()
    # La API actual captura el error y solo imprime un mensaje
    out = capture_stdout(lambda: metro.add_passenger("Juan", "X"))
    assert "Error al agregar pasajero" in out, "Debería mostrar un mensaje de error"
    state = metro.get_state()
    assert "Juan" not in state["passengers"], "Juan no debería estar a bordo"


def test_multiple_passengers_offboarding():
    metro.reset_state()
    metro.add_passenger("Maria", "B")
    metro.add_passenger("Pedro", "B")
    metro.add_passenger("Laura", "C")
    
    metro.move_train()  # A -> B
    state = metro.get_state()
    assert "Maria" not in state["passengers"], "Maria debería haberse bajado"
    assert "Pedro" not in state["passengers"], "Pedro debería haberse bajado"
    assert "Laura" in state["passengers"], "Laura debería seguir a bordo"


def test_circular_route():
    metro.reset_state()
    metro.add_passenger("Carlos", "A")
    
    # Movemos por todas las estaciones (5 estaciones: A, B, C, D, E)
    for _ in range(5):
        metro.move_train()
    
    state = metro.get_state()
    assert state["position"] == "A", "Debería estar de vuelta en la estación A"
    assert "Carlos" not in state["passengers"], "Carlos debería haberse bajado"


def test_remove_nonexistent_passenger():
    metro.reset_state()
    metro.add_passenger("Ana", "B")
    metro.remove_passenger("Inexistente", "B")
    state = metro.get_state()
    assert "Ana" in state["passengers"], "Ana debería seguir a bordo"


if __name__ == "__main__":
    print("🧪 Ejecutando tests genéricos sobre 'metro.py'")
    test_add_and_move()
    print("✅ test_add_and_move aprobado")
    test_remove_passenger()
    print("✅ test_remove_passenger aprobado")
    test_status_output()
    print("✅ test_status_output aprobado")
    test_invalid_destination()
    print("✅ test_invalid_destination aprobado")
    test_multiple_passengers_offboarding()
    print("✅ test_multiple_passengers_offboarding aprobado")
    test_circular_route()
    print("✅ test_circular_route aprobado")
    test_remove_nonexistent_passenger()
    print("✅ test_remove_nonexistent_passenger aprobado")
    print("🎉 ¡Todos los tests fueron aprobados!")
