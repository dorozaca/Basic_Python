def  recursividad(n):
    '''La funcion retorna el factorial de un numero
       n is an int>0
       It returns n! 
    '''
    if n==1:
        return 1

    else:
        return n*recursividad(n-1)    

    
def run():
    n=int(input('Ingrese un numero: '))
    factorial=recursividad(n)
    help(recursividad) # <==IMPORTANTE
    print(factorial)

if __name__== '__main__':
    run()