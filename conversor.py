def conversor(tipo_moneda, cambio):
    pesos = input("Cuantos " + tipo_moneda + " tienes?: ")
    pesos = float(pesos)
    valor_dolar=cambio
    dolares = pesos / valor_dolar
    dolares = round(dolares,3)
    dolares = str (dolares)
    print("Tienes $" + dolares +" dolares") 


menu = input(
    """
    Hello! This is your currency convertor
    
    Please select to type of currency you'd like to convert into USD
    1. COL into USD
    2. PEN into USD
    3. ARG into USD

    Ingresa tu opcion: 

    """
)

option = int(menu)
if option == 1:
    conversor("pesos colombianos", 3765)
elif option ==2:
    conversor("nuevos soles", 4)
elif option==3:
    conversor("pesos argentinos", 67)
else:
    print("Check your choice")


