from typing import List, Dict, Optional
import random
import sys


class Flight:
    def __init__(self, origin: str, destination: str, time: str, fid: int):
        self.origin = origin
        self.destination = destination
        self.time = time
        self.fid = fid

    def __repr__(self):
        return f"Flight({self.fid}: {self.origin} -> {self.destination} @ {self.time})"


class FlightManager:
    def __init__(self):
        self.flights: List[Flight] = []
        self.passengers: Dict[int, List[str]] = {}
        self.debug = False

    def add_flight(self, flight: Flight):
        self.flights.append(flight)
        self.passengers[flight.fid] = []
        print(f"Agregado: {flight}")

    def remove_flight(self, fid: int):
        flight_to_remove = next((f for f in self.flights if f.fid == fid), None)
        if flight_to_remove:
            self.flights.remove(flight_to_remove)
            self.passengers.pop(fid, None)
            print(f"Vuelo {fid} eliminado")
        else:
            print(f"Vuelo {fid} no encontrado")

    def list_flights(self):
        for flight in self.flights:
            print(flight)

    def find_direct_flights(self, origin: str, destination: str) -> List[Flight]:
        return [f for f in self.flights if f.origin == origin and f.destination == destination]

    def find_flights_with_connection(self, origin: str, destination: str) -> List[List[Flight]]:
        results = []
        for f1 in self.flights:
            if f1.origin == origin and f1.destination != destination:
                for f2 in self.flights:
                    if f2.origin == f1.destination and f2.destination == destination:
                        results.append([f1, f2])
        return results

    def show_passengers(self, fid: int):
        print(f"En vuelo {fid}: {self.passengers.get(fid, [])}")

    def unload_passengers(self, fid: int):
        removed = self.passengers.pop(fid, [])
        self.passengers[fid] = []
        print(f"Bajaron todos de {fid}: {removed}")

    def partial_unload(self, fid: int, count: int):
        if fid not in self.passengers:
            print(f"Vuelo no encontrado {fid}")
            return
        current = self.passengers[fid]
        to_remove = current[:count]
        self.passengers[fid] = current[count:]
        print(f"Bajan del vuelo {fid}: {to_remove}")

    def show_flight_time(self, fid: int):
        flight = next((f for f in self.flights if f.fid == fid), None)
        if flight:
            print(f"Tiempo: {flight.time}")
        else:
            print(f"Vuelo {fid} no encontrado")

    def show_connections(self, fid: int):
        flight = next((f for f in self.flights if f.fid == fid), None)
        if not flight:
            return
        mid = flight.destination
        for conn in self.flights:
            if conn.origin == mid:
                print(f"Escala para {fid}: {flight} >> {conn}")


# Iniciamos Testing
if __name__ == "__main__":
    manager = FlightManager()

    # Datos iniciales
    manager.add_flight(Flight("NYC", "LAX", "08:30", 1))
    manager.add_flight(Flight("LAX", "SFO", "12:45", 2))
    manager.add_flight(Flight("NYC", "CHI", "09:00", 3))
    manager.add_flight(Flight("CHI", "LAX", "14:20", 4))
    manager.passengers[1] = ["Ana", "Luis"]
    manager.passengers[2] = ["Pedro"]
    manager.passengers[3] = ["Marta", "Sofía"]
    manager.passengers[4] = ["Juan", "Carlos", "Lucía"]

    print("\n--- Vuelos disponibles ---")
    manager.list_flights()

    print("\n--- Buscar vuelo directo NYC -> SFO ---")
    direct = manager.find_direct_flights("NYC", "SFO")
    print(direct)

    print("\n--- Buscar vuelos con escala NYC -> SFO ---")
    with_conn = manager.find_flights_with_connection("NYC", "SFO")
    for route in with_conn:
        print(f"Ruta con escala: {route[0]} -> {route[1]}")

    print("\n--- Pruebas varias ---")
    manager.add_flight(Flight("SCL", "MEX", "05:55", 5))
    manager.remove_flight(2)
    manager.show_connections(4)
    manager.show_passengers(4)
    manager.show_flight_time(4)
    manager.partial_unload(4, 2)
    manager.show_passengers(4)
    manager.unload_passengers(4)
