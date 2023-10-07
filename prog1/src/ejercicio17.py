## def nombres(nombre,cantidad):
    ## while cantidad > 0:
        ## print(nombre)
        ## cantidad = cantidad -  1

def nombres(nombre,cantidad):
    return (nombre + "\n") * cantidad





if __name__=="__main__":
    nombre= input("Pon tu nombre: ")
    cantidad = int(input("Cuantas veces quieres que se repita: "))
    print(nombres(nombre,cantidad))