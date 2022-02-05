#try catch in C++
#try except and finally in Python


# def divide_lista(lista, divisor):
#     try:
#         return [i/divisor for i in lista]
#     except ZeroDivisionError as e:
#         print(e)
#         return lista


# lista_1 = list(range(20))
# numero=0


# print(divide_lista(lista_1, numero))

def list_division(list,number):
    try:
        return[i/number for i in list]
    except ZeroDivisionError as e:
        print(e)
        return list

my_list=list(range(20))
number=0
print(list_division(my_list, number))
