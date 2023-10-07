def juguetes(payasos,munecas):
    payasos_suma = payasos * 112
    munecas_suma = munecas * 75
    total = payasos_suma + munecas_suma
    return f"{total}"


if __name__=="__main__":
    payasos = int(input("Cuantos payasos: "))
    munecas = int (input("Cuantas muñecas: "))
    print("El total es ",juguetes(payasos,munecas),"g")