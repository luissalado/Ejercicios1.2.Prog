
from src.ejercicio2 import Horas


def test_horas():
    costehoras=10
    horastrabajadas=6
    assert Horas(costehoras,horastrabajadas) == "60" 