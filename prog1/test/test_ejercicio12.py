from src.ejercicio12 import imc


def test_imc():
    peso = 2
    altura = 2
    assert imc(peso,altura) == "0.5"