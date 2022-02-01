# 
#     import random 
# 
# def run():
    
#     number=int(input('Ingresa un numero: '))
#     target=random.randrange(1,100) #Platzi: numero_aleatorio=random.randint(1,100)
#     print(target)

#     while number!= target:
#         if number > target:
#             print('Elige un numero menor')
#         else number < target:
#             print('Elige un numero mayor')
#         number=int(input('Ingresa un numero: '))
#     print('Ganaste')



# if __name__== '__main__':

#     run()




def es_primo():
    number=int(input('Ingrese un numero: '))
    counter=0

    for i in range(1,number+1):
        if i==1 or i==number:
            continue
        if number%i == 0:       #Siempre es con mod, nos preguntamos:cual es el residuo de la division de a entre b
            counter+=1
    
    if counter==0:
        return True
    else:
        return False



def run():
    if es_primo():
        print('Es primo!')
    else:
        print('No es primo')

if __name__== '__main__':
    run()