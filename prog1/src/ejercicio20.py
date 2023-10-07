def telefono(numero):
    return f"Su numero es {numero[4:13]}"

if __name__=="__main__":
    numero = input("Ponga su numero con el siguiente formato (+34-xxxxxxxxxx-56): ")
    partes = numero.split("-")
    if len(partes) == 3 and partes[0] == "+34" and len(partes[1]) == 9 and len(partes[2]) == 2:
        print(telefono(numero))
    else:
        print("El numero esta mal")