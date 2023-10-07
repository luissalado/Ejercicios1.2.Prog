def compra(producto,precio,unidades):
    total = precio * unidades
    return f"{producto} tiene un precio de {precio:09.2f}$, has pedido {unidades:03} y el total del precio seria {total:010.2f}$"


if __name__=="__main__":
    producto = input("Nombre del producto: ")
    precio = float(input ("Precio del producto: "))
    unidades =int(input ("Cuantas unidades desea: "))
    print(compra(producto,precio,unidades))