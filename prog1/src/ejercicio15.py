def ahorros(cantidad):
    interes = 0.04
    primer_año= cantidad * (interes + 1)
    segundo_año =  primer_año * (interes + 1)
    tercer_año = segundo_año * (interes + 1)
    return f"{round(tercer_año,2)}"


if __name__=="__main__":
    cantidad = float(input("Ponga sus ingresos: "))
    print("La cantidad sera: ",ahorros(cantidad))