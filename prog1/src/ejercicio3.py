def expresiones(ancho,alto):
    Primero = ancho / 2
    Segundo = ancho //2
    Tercero = alto / 3
    Suma_multipliacion = 1 + 2 * 5
    return f"Primero: {Primero}, Segundo: {Segundo}, Tercero: {Tercero}, Cuarto: {Suma_multipliacion}" 


if __name__=="__main__":
    ancho = 17
    alto= 12.0
    print(expresiones(ancho,alto))

