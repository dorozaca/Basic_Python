import random

def password_generator():
    numbers=['1','2','3','4','5']
    upper=['A','G','H','R','X']
    lower=['a','d','g','e','h']
    signs=['@','%','$','*','!','?']

    concat=numbers+upper+lower+signs
    password_output=[]

    for i in range(10):
        container=random.choice(concat)
        password_output.append(container)

    password_output="".join(password_output)
    
    return password_output

def run():
    password=password_generator()
    print('Your new password is: '+ password)

if __name__== '__main__':
    run()
