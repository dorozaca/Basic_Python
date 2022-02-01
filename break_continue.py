def run ():
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #         print(contador)
    #     else :
    #         print(contador)

    # for i in range(10000):
        
    #     if i==5678:
    #         break
    #     else:
    #         print(i)


    texto = input ("Ingresa una frase: ")
    for counter in texto:
        if counter == 'a':
            break
        else:
            print(counter)


if __name__== '__main__':
    run()