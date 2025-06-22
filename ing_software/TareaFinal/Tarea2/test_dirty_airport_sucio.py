import main as metro
import importlib
import sys
import io

def reset_state():
    importlib.reload(metro)

def capture_stdout(func, *args, **kwargs):
    buf = io.StringIO()
    old = sys.stdout
    sys.stdout = buf
    try:
        result = func(*args, **kwargs)
    finally:
        sys.stdout = old
    return buf.getvalue(), result

# Tests

def test_add_and_remove():
    reset_state()
    original_count = len(metro.flights)
    new_flight = {'from':'AAA','to':'BBB','time':'01:15','fid':99}
    out, _ = capture_stdout(metro.add, new_flight)
    assert new_flight in metro.flights, "El vuelo nuevo debe agregarse"
    assert 'Agregado' in out, "Debe imprimir 'Agregado'"

    out, _ = capture_stdout(metro.quitar, 99)
    assert all(f.get('fid') != 99 for f in metro.flights), "El vuelo 99 debe eliminarse"
    assert 'Fuera vuelo 99' in out, "Debe imprimir 'Fuera vuelo 99'"
    assert len(metro.flights) == original_count, "Debe volver al conteo original"


def test_escalas_and_flow():
    reset_state()

    out, _ = capture_stdout(metro.ver_escalas, 1)
    assert 'Escala para 1' in out or 'Escala' in out, "Debe mencionar escala"


    out, _ = capture_stdout(metro.quienVa, 4)
    assert 'En vuelo 4' in out, "Debe mencionar 'En vuelo 4'"


    out, _ = capture_stdout(metro.flight_time, 2)
    assert 'Tiempo:' in out, "Debe mencionar 'Tiempo:'"

def test_disembark_partial_and_full():
    reset_state()

    inicial = list(metro.pasajeros[4])

    out, _ = capture_stdout(metro.bajar_algo, 4, 2)
    assert 'Bajan del vuelo 4' in out, "Debe mencionar 'Bajan del vuelo 4'"
    assert len(metro.pasajeros[4]) == max(0, len(inicial) - 2)


    out, _ = capture_stdout(metro.unload, 4)
    assert 'Bajaron todos de 4' in out, "Debe mencionar 'Bajaron todos de 4'"
    assert metro.pasajeros[4] == [], "No debe quedar ningún pasajero"


def test_view_and_main_return():
    reset_state()
    out, ret = capture_stdout(metro.main)
    assert 'Buscando vuelos de' in out
    assert isinstance(ret, int), "main debe devolver un entero"


if __name__ == "__main__":
    print("Ejecutando tests genéricos sobre 'dirty_airport_code.py'")
    for test in [test_add_and_remove, test_escalas_and_flow, test_disembark_partial_and_full, test_view_and_main_return]:
        try:
            test()
            print(f"✅ {test.__name__} passed")
        except AssertionError as e:
            print(f"❌ {test.__name__} failed: {e}")
    print("Tests finalizados")
