def Horas(horastrabajadas,costehoras):
    salario= horastrabajadas * costehoras
    return f"{salario}"

if __name__=="__main__":
    horastrabajadas= int(input("¿Cuantas horas trabajas?: "))
    costehoras = int(input("¿Cuanto cobras por hora?: "))
    print ("importe salaraio",Horas(horastrabajadas,costehoras))

