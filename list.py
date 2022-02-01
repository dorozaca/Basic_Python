def run():
    list1=[1,2,3,4]
    list1[0]=2
    print(list1)

    list2=list(list1) #<== La primera forma de clonar una lista (cuando se clona, diferente ID / objeto)
    print(list2)

    list3=list2[::]#<== La segunda forma de clonar una lista
    print(list3)

    print(id(list1),id(list2),id(list3))

    numbers=list(range(101))
    print(numbers)

    numbers2=list(i**3 for i in numbers)
    print(numbers2)

    numbers3=list(i**2 for i in numbers2 if i%2!=0)
    print(numbers3)

    list_total=[list1,list2,list3]
    print(list_total)

    for i in list_total:
        print(id(i))
    


if __name__== '__main__':
    run()