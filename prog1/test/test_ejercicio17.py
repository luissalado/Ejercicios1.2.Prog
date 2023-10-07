from src.ejercicio17 import nombres


def test_nombres():
    nombre = "luis"
    cantidad = 10
    assert nombres(nombre,cantidad) == "luis\nluis\nluis\nluis\nluis\nluis\nluis\nluis\nluis\nluis\n"