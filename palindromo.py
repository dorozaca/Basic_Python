def palindromo(palabra):
    palabra=palabra.replace(" ","")
    palabra=palabra.lower()
    if palabra == palabra[::-1]:
        return True
    else:
        return False

    
def run():
    palabra = input("Ingrese una palabra: ")
    es_palabra=palindromo(palabra)
    if es_palabra == True:
        print("Es palindromo!")
    else:
        print("No es palindromo!")


if __name__== '__main__':
    run()