#solucion mas limpia

number=int(input('Enter a number: '))
epsilon=0.01
base=0.0

while (number-base**2)>=epsilon: #el loop solo termina cuando la diferencia es menor a epsilon
    base+=epsilon**2             #por lo tanto ya tengo la respuesta

print(f'{base} is square root of {number} with {epsilon} Approx. error')


# objetivo=int(input('Escoge un numero: '))
# epsilon= 0.01
# paso = epsilon**2
# respuesta=0.0

# while abs(respuesta**2 - objetivo) >= epsilon and respuesta<=objetivo: #solo aceptamos una respuesta**2 que se distancia del objetivo en un valor menor a 0.01
#         print(abs(respuesta**2 - objetivo), respuesta)
#         respuesta+=paso

# if abs(respuesta**2 - objetivo) >= epsilon: #si sucede esto significa que nuestra aproximacion todavia es muy grande (el profe hizo este if por las wevas) 
#    print(f'No se encontro la raiz cuadrada de {objetivo}') 

# else:
#     print(f'La raiz cuadrada de {objetivo} es {respuesta}') #esto debio ir de frente

#aca una buena explicacion de un chul:
# En el while, lo que sucede es que en la primera iteración, la diferencia abs(respuesta^2- objetivo) va a ser mucho mayor a epsilon, entonces, a medida que pasan las iteraciones, el valor de respuesta va aumentando a razón paso = 0.0001 y por ende la diferencia abs(respuesta^2-objetivo) se va haciendo mas pequeña.
# El ciclo while va a terminar justo en el momento en que la diferencia abs(respuesta^2-objetivo) sea apenitas menor que epsilon.
# <br>
# Hasta este punto ya tenemos un numero el cual al elevarlo al cuadrado se aproxima a objetivo con un ligero error menor a epsilon, y lo que sigue es simplemente confirmarlo mediante un código usando if statement.
# “nosotros sabemos que ya tienes la respuesta aproximada” y con el código de if solo haremos que la computadora nos muestre “algo” si nuestra condición principal es verdadera o True.

# if si la diferencia abs(respuesta^2-objetivo) es mayor o igual a epsilon, entonces tenemos un error mayor al que nosotros queriamos y por eso decimos que No se contró la raíz cuadrada de {objetivo}
# else si la diferencia no es mayor o igual, entonces es una afirmacion de que es menor a epsilon y eso si nos interesa y por eso decimos que La raiz cuadrada de {objetivo} es {respuesta}
# <br>
# Espero a alguien le haya servido esta explicación. saludos