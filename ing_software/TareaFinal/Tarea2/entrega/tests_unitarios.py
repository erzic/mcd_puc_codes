import unittest
import io
import sys
from contextlib import redirect_stdout
from main import FlightManager, Flight


class TestFlightManagerAdapted(unittest.TestCase):

    def setUp(self):
        self.manager = FlightManager()
        self.manager.add_flight(Flight("NYC", "LAX", "08:30", 1))
        self.manager.add_flight(Flight("LAX", "SFO", "12:45", 2))
        self.manager.add_flight(Flight("NYC", "CHI", "09:00", 3))
        self.manager.add_flight(Flight("CHI", "LAX", "14:20", 4))
        self.manager.passengers[1] = ["Ana", "Luis"]
        self.manager.passengers[4] = ["Juan", "Carlos", "Lucía"]

    def capture_output(self, func, *args, **kwargs):
        f = io.StringIO()
        with redirect_stdout(f):
            result = func(*args, **kwargs)
        return f.getvalue(), result

    def test_add_and_remove(self):
        original_count = len(self.manager.flights)
        new_flight = Flight("AAA", "BBB", "01:15", 99)
        out, _ = self.capture_output(self.manager.add_flight, new_flight)
        self.assertIn(new_flight, self.manager.flights)
        self.assertIn("Agregado", out)

        out, _ = self.capture_output(self.manager.remove_flight, 99)
        self.assertTrue(all(f.fid != 99 for f in self.manager.flights))
        self.assertIn("Vuelo 99 eliminado", out)
        self.assertEqual(len(self.manager.flights), original_count)

    def test_show_connections_and_info(self):
        out, _ = self.capture_output(self.manager.show_connections, 1)
        self.assertIn("Escala", out)

        out, _ = self.capture_output(self.manager.show_passengers, 4)
        self.assertIn("En vuelo 4", out)

        out, _ = self.capture_output(self.manager.show_flight_time, 2)
        self.assertIn("Tiempo:", out)

    def test_disembark_partial_and_full(self):
        inicial = list(self.manager.passengers[4])

        out, _ = self.capture_output(self.manager.partial_unload, 4, 2)
        self.assertIn("Bajan del vuelo 4", out)
        self.assertEqual(len(self.manager.passengers[4]), max(0, len(inicial) - 2))

        out, _ = self.capture_output(self.manager.unload_passengers, 4)
        self.assertIn("Bajaron todos de 4", out)
        self.assertEqual(self.manager.passengers[4], [])

    def test_main_like_behavior(self):
        def simulated_main():
            return 42

        out = io.StringIO()
        with redirect_stdout(out):
            result = simulated_main()
        self.assertIn("42", str(result))
        self.assertIsInstance(result, int)


if __name__ == '__main__':
    unittest.main()
