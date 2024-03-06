"""
Cria uma lista de valores de propriedades (imoveis) , a partir dessa lista acesse o 3 elemento , depois adicione um
elemento , depois faca uma copia (deep copy) e a partir da copia voce vai remover o 2 elemento . no final , imprima
a copia e a lista antiga.
"""

imoveis = [125000, 200000, 300000]
print(imoveis)
print(imoveis[2])
imoveis.append(500000)
print(imoveis)
imoveis = [125000, 200000, 300000]
copia = imoveis.copy()
copia.remove(200000)
print(imoveis)
print(copia)
