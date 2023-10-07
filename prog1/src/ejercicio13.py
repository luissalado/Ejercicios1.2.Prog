def operacion3(num1,num2):
    operacion = int(num1 / num2)
    operacion2 = int(num1 % num2)
    return f"la división de {num1} entre {num2} da un cociente {operacion} y un resto {operacion2}, donde {num1} y {num2} son los números introducidos por el usuario, y {operacion} y {operacion2} son el cociente y el resto de la división entera respectivamente"


if __name__=="__main__":
    num1 = int(input("Dime un numero: "))
    num2 = int(input("Dime un numero: "))
    print(operacion3(num1,num2))