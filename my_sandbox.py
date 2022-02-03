#guess the number game
# import random

# def run():
#     number=int(input('Guess the number: '))
#     target_number=random.randint(1,100)

#     while number!=target_number:
#         if number>target_number:
#             print('Choose a smaller number: ')
#         if number<target_number:
#             print('Choose a bigger number: ')
#         number=int(input('Guess the number: '))

#     print('You Win!')

# if __name__== '__main__':
#     run()


#prime numbers detector

# def is_prime():
#     number=int(input('Enter a number: '))
#     counter=0

#     for i in range (1,number+1):
#         if i==1 or i==number:
#             continue
#         if (number%i)==0:
#             counter+=1
#     if counter==0:
#         return True
#     if counter!=0:
#         return False


# def run():
#     if is_prime():
#         print('It is prime!')
#     else:
#         print('It is not prime!')

# if __name__=='__main__':
#     run()


# #password_generator

# import random

# def password_generator():
#     numbers=['5','6','7','8']
#     upper=['A','D','G','E']
#     lower=['d','r','t','e']
#     symbols=['#','$','%','@']

#     concat=numbers+upper+lower+symbols
#     password=[]

#     for i in range(12):
#         container=random.choice(concat)
#         password.append(container)

#     password="".join(password)
#     return password

# def run():
#     password=password_generator()
#     print('Your new password is '+password)

# if __name__=='__main__':
#     run()

# counter=0
# my_number=int(input('Ingrese un numero: '))

# while counter**2<my_number:
#     counter+=1
# if counter**2==my_number:
#     print(f'La raiz cuadrada de {my_number} es {counter} ')
# else:
#     print(f'{my_number} no tiene una raiz cuadrada exacta')

#Aproximacion de soluciones (mi solucion - error)
# number=int(input('Ingrese un numero: '))
# epsilon=0.01
# base=0.0

# while abs((number-base**2)>=epsilon) and base**2<number:
#     print((number-base**2), base)
#     base +=epsilon
    

# if abs(number-base**2)<epsilon:
#     print (f'La raiz cuadrada de {number} es {base}')
# else:
#     print (f'{number} no tiene una raiz cuadrada exacta')

#Aproximacion de soluciones (mi solucion - corregida)

# number=int(input('Enter a number: '))
# epsilon=0.01
# base=0.0

# while (number-base**2)>=epsilon: #el loop solo termina cuando la diferencia es menor a epsilon
#     base+=epsilon**2

# print(f'{base} is square root of {number} with {epsilon} Approx. error')

# binary search finding index
# def run():
#     my_array=[2,4,6,8,10,12,14,16,18,20]
#     low=0
#     high=len(my_array)-1
#     mid=low+(high-low)//2
#     number=int(input('Enter number for which we will find its position: '))
#     counter=0

#     while low<=high:
#         if number==my_array[mid]:
#             print(f'Number\'s positon is {mid}')
#             counter +=1
#             break

#         elif number>my_array[mid]:
#             low=mid+1

#         else:
#             high=mid-1

#         mid=low+(high-low)//2

#     if counter==0:
#         print('Number is not whithin the list')

# if __name__=='__main__':
#     run()


#Binary Search with approx.  
# def run():
#     number=int(input('Enter number: '))
#     low=0.0
#     high=max(1.0,number)
#     base=(low+high)/2
#     epsilon=0.01

#     while abs(base**2-number)>=epsilon:
#         if number<base**2:
#             high=base

#         else:
#             low=base

#         base=(low+high)/2

#     print(f'Square root of {number} is {base}')


# if __name__== '__main__':
#     run()

 

 

 



