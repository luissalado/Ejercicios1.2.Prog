def email(correo):
    partes = correo.split("@")
    if partes[1] != ("ceu.es"):
        partes[1] = ("ceu.es")
    return f"{partes[0]}@{partes[1]}"


if __name__=="__main__":
    correo = input("Ponga su correo: ")
    print(email(correo))