from src.ejercicio5 import Calculo

def test_calculo():
    precio = 4
    assert Calculo(precio) == "4.68"