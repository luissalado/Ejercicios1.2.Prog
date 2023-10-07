from src.ejercicio16 import panaderia


def test_panaderia():
    cantidad = 10
    assert panaderia(cantidad) == "El precio habitual es 3.49, al no estar frescas, se le hace un 60%, el total del precio despues del 60% es 12.094"