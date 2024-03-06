"""
Crie uma tupla de sabores de sorvetes e depois faca o desempacotamento dessa tupla, depois disso itere sobre a tupla
e na hora de iterar voce vai imprimir o sabor apenas se o sabor for chocolate, depois adicione um sabor e no final
faca um slicing do segundo elemento ao quarto
"""

sabores = 'chocolate', 'creme', 'misto', 'morango', ' amendoim'
#adicionar morango

sabor1, sabor2, sabor3, sabor4, sabor5 = sabores
print(sabores)
for sabor in sabores:
    if sabor == 'chocolate':
        print(sabor)
""""    
copiasabores = sabores
copiasabores.append('morango')
print(copiasabores)

NAO DA PRA ADICIONAR NA TUPLA
"""

print(sabores[2:])