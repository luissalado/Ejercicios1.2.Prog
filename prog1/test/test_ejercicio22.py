from src.ejercicio22  import cambio


def test_cambio():
    frase = "alberto"
    vocal = "a"
    assert cambio(frase,vocal) == "Alberto"