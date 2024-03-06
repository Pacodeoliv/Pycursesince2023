"""
Crie uma tupla de animais e a partir dela crie uma cópia, (usando a cópia) faça um slicing do terceiro animal ao
quinto, em seguida itere sobre a tupla e imprima o animal apenas se for "cachorro", no final acesse o quinto elemento.
"""
tupla1 = ( 'gato','cachorro', 'cobra', 'zebra', 'aranha', 'aguia' )
copia = tupla1
print(copia[2:5])
for animal in copia:
     if animal == 'cachorro':
        print(animal)
print(copia[4])


"""tupla1 = ( 'gato','cachorro', 'cobra', 'zebra', 'aranha', 'aguia' )
copia = tupla1
print(copia[2:5])
    for cachorro in copia:
        cachorro = ('cachorro')
        if  copia = cachorro
        print(copia)
        
CODIGO ERRADO 
        """






