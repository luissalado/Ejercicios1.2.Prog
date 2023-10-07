def pregunta(nombre):
    longiutd = len(nombre)
    mayus = nombre.upper()
    return f"{mayus} tiene {longiutd} letras."

if __name__=="__main__":
    nombre = input("Dime tu nombre: ")
    print(pregunta(nombre))

