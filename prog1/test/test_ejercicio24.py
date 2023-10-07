from src.ejercicio24 import precio

def test_precio():
    moneda = 10.547
    assert precio(moneda) == "10 euros y 55 centimos"