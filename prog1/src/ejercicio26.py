def compra(productos):
    producto_final = productos.replace(",","\n")
    return f"{producto_final}"


if __name__=="__main__":
    productos = input("Escribe su compra seaparando los productos por comas: ")
    print(compra(productos))





