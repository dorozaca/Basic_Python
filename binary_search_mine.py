# def run():
    
# Finding number with binary search:
#     
# my_array=[]
#     for i in range(10):
#         container=int(input('Enter a number: '))
#         my_array.append(container)

#     print(my_array)
#     number=int(input('What number you want to search for: '))
#     low=0
#     high=len(my_array)-1
#     mid=low+(high-low)//2
    
#     counter=0

#     while low<=high:
#         if number==my_array[mid]:
#             print(f'El numero {number} esta en la posicion {mid}')
#             counter +=1
#             break

#         elif number>my_array[mid]:
#             low=mid+1

#         else:
#             high=mid-1

#         mid=low + (high-low)//2

#     if counter==0:
#         print('The number is not in the list')

# if __name__== '__main__':
#     run()


##Square root with approx and binary search


def run():
    number=int(input('Enter number: '))
    low=0.0
    high=max(1.0,number)
    base=(low + high)/2
    error= 0.01

    while abs(base**2-number)>=error:
        if base**2>number:
            high=base

        else:
            low=base

        base=(low + high)/2

    print(f'Square root of {number} is {base}')    

if __name__== '__main__':
    run()