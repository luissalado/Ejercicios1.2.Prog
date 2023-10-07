from src.ejercicio20  import telefono

def test_telefono():
    numero = "+34-698569874-56"
    assert telefono(numero) == "Su numero es 698569874"