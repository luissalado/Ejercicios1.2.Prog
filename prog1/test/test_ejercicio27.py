from src.ejercicio27 import compra


def test_compra():
    producto = "papa"
    precio = 12.587465718
    unidades = 78
    assert compra(producto,precio,unidades) == "papa tiene un precio de 000012.59$, has pedido 078 y el total del precio seria 0000981.82$"