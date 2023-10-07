from src.ejercicio6 import calcula

def test_calcula():
    precio = 4.0
    assert calcula(precio) == f"El precio sin iva es 4.0, y con el iva aplicado, se queda en 4.4"