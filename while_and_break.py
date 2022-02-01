def run():
    number = int(input("ingresa un numero: ")) 
    counter = 0
    LIMIT = 20    
    while number < LIMIT:
        print(counter)
        counter +=1
        if counter == 15:
            break
        
            

if __name__== '__main__':
    run()
