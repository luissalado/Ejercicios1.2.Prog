from src.ejercicio14 import juguetes

def test_juguetes():
    muñecas = 5
    payasos = 5
    assert juguetes(muñecas,payasos) == "935"