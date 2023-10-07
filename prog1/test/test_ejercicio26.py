from src.ejercicio26 import compra

def test_compra():
    productos= "fresa,platano,mago,girasol"
    assert compra(productos) == "fresa\nplatano\nmago\ngirasol"