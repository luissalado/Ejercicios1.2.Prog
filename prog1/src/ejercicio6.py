def calcula(precio):
    iva = precio * 10/100
    total = precio + iva
    return f"El precio sin iva es {precio}, y con el iva aplicado, se queda en {total}"


if __name__=="__main__":
    precio = precio = float(input("¿Cual es el precio del producto del iva?: "))
    print(calcula(precio))
