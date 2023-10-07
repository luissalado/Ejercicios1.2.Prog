def analiza(frase):
    return f"La frase invertida es {frase[::-1]}"



if __name__=="__main__":
    frase = input("Dime una frase para invertirla: ")
    print(analiza(frase))