from src.ejercicio19 import pregunta


def test_pregunta():
    nombre = "luis"
    assert pregunta(nombre) == "LUIS tiene 4 letras."