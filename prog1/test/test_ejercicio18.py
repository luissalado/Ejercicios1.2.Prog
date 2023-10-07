from src.ejercicio18 import gramatica


def test_gramatica():
    nombre_completo ="Luis Salado Moran"
    assert gramatica(nombre_completo) == "LUIS SALADO MORAN\nluis salado moran\nLuis Salado Moran\n"