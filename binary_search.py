# def run():
#     my_array=[25,32,44,58,76,88,89,90,91,99, 101, 123, 156]
#     number=int(input('Por favor ingrese el numero: '))
#     low = 0
#     high = len(my_array)-1
#     mid = low + (high-low)//2
#     counter=0


#     while low <= high:
#         if number == my_array[mid]:
#             print(f'El indice del numero es {mid}')
#             counter+=1
#             break

#         elif number > my_array[mid]:
#             low=mid+1

#         else:
#             high=mid-1
        
#         mid = low + (high-low)//2

#     if counter == 0:
#         print('El numero no fue encontrado en la lista')
    

# if __name__== '__main__':
#     run()

# def run():
#     number=int(input('Enter number: '))
#     low= 0.0
#     high=max(1.0, number)
#     base = (low + high)/2
#     error = 0.0001
    

#     while abs(base**2-number)>=error:
#         print(f'number:{number}, base:{base}, low:{low}, high:{high}, error:{abs(base**2-number)}')
#         if base**2>number:
#             high=base

#         else:
#             low=base

#         base = (low + high)/2


#     print(f'La raiz cuadrada de {number} es {base} y el error final es {abs(base**2-number)}')

# if __name__== '__main__':
#     run()

