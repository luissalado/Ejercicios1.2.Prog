from src.ejercicio25 import fecha


def test_fecha():
    nacimiento = "1/1/2002"
    assert fecha(nacimiento) == "Dia: 1 Mes:1 Año:2002"