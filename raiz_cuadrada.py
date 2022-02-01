counter=0
my_number=int(input('Ingrese un numero: '))

while counter**2<my_number: #tiene que ser < porque si fuese <= subiria el counter uno mas cuando es igual
    counter+=1              #y la respuesta seria erronea. Tiene que parar en cuanto counter es = or > k number (cuaderno)
if counter**2==my_number:
    print(f'La raiz cuadrada de {my_number} es {counter} ')
else:
    print(f'{my_number} no tiene una raiz cuadrada exacta')
    