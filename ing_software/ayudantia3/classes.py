# classes.py
from typing import List, Dict

class Passenger:
    """Representa a un pasajero con nombre y destino."""
    def __init__(self, name: str, destination: str):
        self.name = name
        self.destination = destination
        
class MetroSystem:
    """Encapsula la lógica y el estado interno del sistema de metro."""
    def __init__(self, stations: List[str]) -> None:
        if not stations:
            raise ValueError("Debe haber al menos una estación.")
        self.__stations = stations
        self.__current_idx = 0
        self.__passengers: List[Passenger] = []

    def reset(self) -> None:
        """Reinicia la posición al inicio y vacía la lista de pasajeros."""
        self.__current_idx = 0
        self.__passengers.clear()

    def add_passenger(self, passenger: Passenger) -> None:
        """Sube un pasajero validando que su destino exista."""
        if passenger.destination not in self.__stations:
            raise ValueError(f"Destino inválido: {passenger.destination}")
        self.__passengers.append(passenger)

    def move_to_next_station(self) -> None:
        """Avanza a la siguiente estación (cíclico)."""
        self.__current_idx = (self.__current_idx + 1) % len(self.__stations)

    def get_offboarding_passengers(self) -> List[Passenger]:
        """
        Devuelve la lista de pasajeros que deben bajar aquí.
        """
        station = self.current_station
        # Selecciona y retira pasajeros que lleguen a esta estación
        offboarding = [p for p in self.__passengers if p.destination == station]
        self.__passengers = [p for p in self.__passengers if p.destination != station]
        return offboarding
    
    def remove(self, name: str, at_station: str) -> None:
        self.__passengers = [
            p for p in self.__passengers
            if not (p.name == name and p.destination == at_station)
        ]

    @property
    def current_station(self) -> str:
        """Nombre de la estación actual."""
        return self.__stations[self.__current_idx]

    def get_state(self) -> Dict[str, object]:
        """Devuelve la estación actual y la lista de nombres de pasajeros a bordo."""
        return {
            "position": self.current_station,
            "passengers": [p.name for p in self.__passengers],
        }
