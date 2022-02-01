import math

def aplicar_operaciones(num):
    operaciones=[abs,float,math.sqrt]

    resultado=[]
    for i in operaciones:
        container=i(num)
        resultado.append(container)

    return resultado


def run():
    n=int(input('Ingrese numero: '))
    answer=aplicar_operaciones(n)
    print(answer)

if __name__=='__main__':
    run()


