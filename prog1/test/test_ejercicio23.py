from src.ejercicio23 import email

def test_correo ():
    correo = "luis@gmail.com"
    assert email(correo) == "luis@ceu.es"