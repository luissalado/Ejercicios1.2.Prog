def cambio(frase,vocal):
    frase_completa = frase.replace(vocal.lower(),vocal.upper())
    return f"{frase_completa}"


if __name__=="__main__":
    frase = input("Introduzca una frase: ")
    vocal = input("introduzca una vocal: ")
    if vocal in "aeiouAEIOU":
        print(cambio(frase,vocal))
    else:
        print("Prueba otra vez")