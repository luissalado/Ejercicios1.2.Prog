def imc(peso,altura):
    formula = peso / (altura**2)
    return f"{formula}"


if __name__=="__main__":
    peso = float(input("Ponga su peso en kg: "))
    altura = float(input("Ponga su altura en metros: "))
    print("Su imc es ",imc(peso,altura))