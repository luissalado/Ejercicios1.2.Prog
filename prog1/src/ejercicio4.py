def Convertir(grados):
    celsisus  = (grados * 9/5) + 32
    return f"{celsisus}"


if __name__=="__main__":
    grados = float(input("Dime la temperatura en celsius: "))
    print("Resultado: ",Convertir(grados))



