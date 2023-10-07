def operacion2(numero):
    suma = int((numero*(numero+1)) / 2)
    return f"{suma}"

if __name__=="__main__":
    numero  = int(input("Dime un numero: "))
    print("La suma sera: ",operacion2(numero))