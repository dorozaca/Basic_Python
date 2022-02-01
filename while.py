# contador = 0
# print(2**contador)
# contador = 1
# print(2**contador)
# contador = 2
# print(2**contador)
# contador = 3
# print(2**contador)

def run():
    LIMIT = 100000
    counter = 0
    potency=2**counter

    while LIMIT > potency:
        print("2 to the power "+ str(counter) + " is equal to " + str(potency))
        counter = counter + 1
        potency = 2**counter 


if __name__== '__main__':
    run()
