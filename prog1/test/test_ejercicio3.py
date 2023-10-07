from src.ejercicio3 import expresiones

def test_expresiones():
    ancho = 17
    alto = 12.0
    assert expresiones(ancho,alto) == "Primero: 8.5, Segundo: 8, Tercero: 4.0, Cuarto: 11"