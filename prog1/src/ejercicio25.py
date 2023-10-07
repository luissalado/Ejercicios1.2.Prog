def fecha(nacimiento):
    partes = nacimiento.split("/")
    return f"Dia: {partes[0]} Mes:{partes[1]} Año:{partes[2]}"

if __name__=="__main__":
    nacimiento = input("Pon una fecha con el siguiente formato (XX/XX/XXXX): ")
    print(fecha(nacimiento))