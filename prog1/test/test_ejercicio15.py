from src.ejercicio15 import ahorros


def test_ahorros():
    cantidad = 10
    assert ahorros(cantidad) == "11.25"