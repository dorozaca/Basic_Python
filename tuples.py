my_tuple=()
print(f'my_tuple() - vacio: {my_tuple}')

my_tuple=(1,'dos',True)
print(f'my_tuple() con datos: {my_tuple}')
print(f'my_tuple[0]: {my_tuple[0]}') #igual que array podemos invocar elementos por le indice
print()

my_array=[1,2,3]
print(f'my_array: {my_array}')
print(f'my_array[0]: {my_array[0]}')
print()
#my_tuple[0]=1
#print(my_tuple[0]) <== Se tiene que reasignar la tupla (toda) sino error

my_tuple=(1)        #<== No es tupla, se queda en integer   
print(f'my_tuple=(1): {type(my_tuple)}')  
my_tuple=(1,)       #<==Si es tupla, se necesita agregar una coma , IMPORTANTE
print(f'my_tuple=(1,): {type(my_tuple)}')  
print()

my_second_tuple=(2,3,4,5)
print(f'my second tuple: {my_second_tuple}')
print(f'my first tuple: {my_tuple}')
my_tuple += my_second_tuple #<==Se pueden sumar tuplas
print(f' my_tuple += my_second_tuple: {my_tuple}')
print()

x,y,z,w,a = my_tuple #<== Se necesitan asignar todos los valores de la tupla, no solo los 3 primeros
print(f'x,y,z = my_tuple: x={x},y={y},z={z}')
print()

def coordenadas():
    return (5,4) #<==Se puede retornar una tupla, se necesita usar parentesis

mi_ubicacion=coordenadas()
print(f'mi_ubicacion = coordenadas(): {mi_ubicacion}')

x,y=coordenadas() #<== Tambien se pueden asignar variables individuales directamente al resultado de la funcion
print(f'x,y=coordenadas(): {x},{y}')




