def primera_letra(lista):
    letras=[]
    for i in lista:
        assert type(i) == str, f'{i} no es string'
        assert len(i) >0,'Can\'t accept void words'

        letras.append(i[0])
    return letras

mi_lista=['Jose',3,'Miguel','Paolo','Jefferson']
minus=list(i.lower() for i in primera_letra(mi_lista))
print(minus)

