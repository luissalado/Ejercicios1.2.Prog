from src.ejercicio1 import Nombre

def test_nombre():
    nombre = "luis"
    assert Nombre(nombre) ==  "hola,luis"