def run():
    mi_diccionario={
        'Argentina': 500,
        'Peru': 400,
        'Colombia': 600,
    }

    print(mi_diccionario['Peru']) #<==Buscando termino se usa corchetes
    print(mi_diccionario.get('Venezuela',900)) #<==Buscando termino con backup - parentesis
    mi_diccionario['Jaime']=700 #<== Asignando nuevo termino
    mi_diccionario['Peru']=200 #<== Cambiando termino
    del mi_diccionario['Jaime'] #<== Borrando termino


    for paises, income in mi_diccionario.items():
        print(paises +", "+ str(income))
        
    print()

    for paises in mi_diccionario.keys():
        print(paises)
    
    print()

    for income in mi_diccionario.values():
        print(income)



if __name__== '__main__':
    run()