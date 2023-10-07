def precio(moneda):
    moneda = round(moneda,2)
    partes = str(moneda).split(".")
    return f"{partes[0]} euros y {partes[1]} centimos"

if __name__=="__main__":
    moneda = float(input("Cual es el precio del producto: (xx.xx) "))
    print(precio(moneda))