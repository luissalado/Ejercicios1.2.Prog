def panaderia(cantidad):
    precio = 3.49
    fresco = precio * 60/100
    print(fresco)
    total = cantidad + fresco
    return f"El precio habitual es {precio}, al no estar frescas, se le hace un 60%, el total del precio despues del 60% es {total}"



if __name__=="__main__":
    cantidad= int(input("Dime cuantos panes quieres: "))
    print(panaderia(cantidad))