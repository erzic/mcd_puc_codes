import unittest
from main import Flight, FlightManager


class TestFlightManager(unittest.TestCase):

    def setUp(self):
        self.manager = FlightManager()
        self.manager.add_flight(Flight("NYC", "LAX", "08:30", 1))
        self.manager.add_flight(Flight("LAX", "SFO", "12:45", 2))
        self.manager.add_flight(Flight("NYC", "CHI", "09:00", 3))
        self.manager.add_flight(Flight("CHI", "LAX", "14:20", 4))
        self.manager.passengers[1] = ["Ana", "Luis"]
        self.manager.passengers[4] = ["Juan", "Carlos", "Lucia"]

    def test_add_flight(self):
        self.assertEqual(len(self.manager.flights), 4)

    def test_remove_flight(self):
        self.manager.remove_flight(2)
        self.assertEqual(len(self.manager.flights), 3)
        self.assertNotIn(2, self.manager.passengers)

    def test_find_direct_flight(self):
        result = self.manager.find_direct_flights("NYC", "LAX")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].fid, 1)

    def test_find_flight_with_connection(self):
        result = self.manager.find_flights_with_connection("NYC", "SFO")
        self.assertTrue(any(f[0].fid == 1 and f[1].fid == 2 for f in result))

    def test_show_passengers(self):
        self.assertListEqual(self.manager.passengers[1], ["Ana", "Luis"])

    def test_unload_passengers(self):
        self.manager.unload_passengers(1)
        self.assertListEqual(self.manager.passengers[1], [])

    def test_partial_unload(self):
        self.manager.partial_unload(4, 2)
        self.assertListEqual(self.manager.passengers[4], ["Lucia"])

    def test_show_flight_time(self):
        flight = next((f for f in self.manager.flights if f.fid == 3), None)
        self.assertEqual(flight.time, "09:00")

    def test_passenger_list_remains(self):
        self.manager.partial_unload(4, 1)
        self.assertEqual(self.manager.passengers[4], ["Carlos", "Lucia"])

    def test_connection_existence(self):
        connections = self.manager.find_flights_with_connection("NYC", "LAX")
        self.assertTrue(len(connections) > 0)


if __name__ == '__main__':
    unittest.main()
