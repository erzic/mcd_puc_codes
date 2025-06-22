# api.py
from classes import MetroSystem, Passenger

# Instancia singleton del sistema
_metro = MetroSystem(["A", "B", "C", "D", "E"])


def reset_state() -> None:
    """Reinicia el sistema de metro."""
    _metro.reset()
    print("Sistema de metro reiniciado en estación A.")


def add_passenger(name: str, destination: str) -> None:
    """Sube un pasajero al metro e informa por consola."""
    try:
        passenger = Passenger(name, destination)
        _metro.add_passenger(passenger)
        print(f"Sube {name} en {_metro.current_station}, destino {destination}.")
    except ValueError as e:
        print(f"Error al agregar pasajero: {e}")

def remove_passenger(name: str, at_station: str) -> None:
    _metro.remove(name, at_station)
    print(f"{name} removido en {at_station}.")

def move_train() -> None:
    """
    Avanza el tren, procesa bajadas e imprime en consola
    quién baja y en qué estación.
    """
    _metro.move_to_next_station()
    off = _metro.get_offboarding_passengers()
    print(f"Metro va a {_metro.current_station}.")
    for p in off:
        print(f"Baja {p.name} en {_metro.current_station}.")


def get_state() -> dict:
    state = _metro.get_state()
    print(f"Estación actual: {state['position']}")
    print("Pasajeros a bordo:", ", ".join(state["passengers"]) or "— ninguno —")
    return state
    