# external_counter=0
# internal_counter=0

# counter=0
# diego=[1,45,65,89,2,64]
# premio=[2,64,40,78,5,11]


# while external_counter<6: #Tiene que ser igual a len(list)
#     while internal_counter<6:
#         if diego[external_counter]==premio[internal_counter]:
#             counter+=1
#         internal_counter+=1

#     external_counter+=1
#     internal_counter=0

# print(counter)


def run():
   
    print('Enter your guessing numbers: ')
    my_numbers=[]
    for i in range(6):
        container=int(input('Enter number '+str(i+1)+': '))
        my_numbers.append(container)

    print('These are your numbers: ' + str(my_numbers))
    print()
    print('Now enter Mega Million winner numbers: ')

    mega_millions=[]
    
    for i in range(6):
        container2=int(input('Enter number '+str(i+1)+': '))
        mega_millions.append(container2)

    print('These are your Mega Million numbers: ' + str(mega_millions))
    print()

    
    #mega_millions=[4,19,39,42,52,9]
    counter = 0
   
    for i in range(6):
        for j in range(6):
            if mega_millions[i]==my_numbers[j]:
                counter+=1

    if counter == 0:
        print('No matches at all')
    else:
        print('You matched: '+str(counter)+' numbers!')
    
    print()

        


if __name__=='__main__':
    run()