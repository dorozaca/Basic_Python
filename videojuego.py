from random import random


def numero():
    numero_ingresado = int(input("Elige un numero del 1 al 100: "))
    return numero_ingresado


def run():
    
    NUMERO_TARGET = int(random()*100)
    print(NUMERO_TARGET)
    mi_numero=numero()
    if  mi_numero==NUMERO_TARGET:
        print("Ganaste")
    else: 
        while mi_numero != NUMERO_TARGET:
            if mi_numero < NUMERO_TARGET:
                print("Busca un numero mas grande")
                numero()
            elif mi_numero > NUMERO_TARGET:
                print("Busca un numero mas pequeño")
                numero()

        
if __name__== '__main__':
    run()