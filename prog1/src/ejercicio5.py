def Calculo(precio):
    iva = precio * 17/100
    total= precio + iva
    return f"{total}"


if __name__=="__main__":
    precio = float(input("¿Cual es el precio del producto del iva?: "))
    print("total:",Calculo(precio))



