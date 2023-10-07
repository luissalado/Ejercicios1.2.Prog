from src.ejercicio21 import analiza


def test_analiza():
    frase = "felipe es"
    assert analiza(frase) == "La frase invertida es se epilef"