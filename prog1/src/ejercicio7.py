def solicita(num1,num2,num3):
    suma = num1 + num2 + num3
    return f"{suma}"

if __name__=="__main__":
    num1 = float(input("dime un numero: "))
    num2 = float(input("dime un numero: "))
    num3 = float(input("dime un numero: "))
    print("La suma es", solicita(num1,num2,num3))