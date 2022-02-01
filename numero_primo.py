
def es_primo(numero):
    counter = 0                 # We need to use counter variable to contro whether if statements are valid
    for i in range(1,numero +1 ): 
        if i == 1 or i == numero: 
            continue            # we use continue when we need to jump over any conditions, like common conditions to every number 
        if numero % i == 0:
            counter +=1         #If condition is valid we update counter varianle
    if counter == 0:
        return True             #It is important to use RETURN here to pass along the "True" parameter
    else:
        return False

      
def run():
    numero = int(input("Input a number: "))
    if es_primo(numero):
        print("Es primo")
    else:
        print("No es primo!")
        

if __name__== '__main__':
    run()