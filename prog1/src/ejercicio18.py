def gramatica(nombre_completo):
    mayus = nombre_completo.upper()
    minus = nombre_completo.lower()
    Completo = nombre_completo.title()
    return (mayus + "\n" + minus + "\n" + Completo + "\n")






if __name__=="__main__":
    nombre_completo=input("Ponga su nombre completo: ")
    print(gramatica(nombre_completo))