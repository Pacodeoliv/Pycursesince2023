"""
Crie um ordered dict que tenha como parametro o nome de um remedio e tenha como valor quantas vezes ele foi comprado,
leia do usuario 5 elementos e adicione no dicionario , e partir disso faca um shallowcopy . No final itere usando a
copia
"""


from collections import OrderedDict
remedios = OrderedDict()

#Receba do usuario (Parametro com valores + soma de quantas vezes se repete)
for i in range(5):
    nomedoremedio = input("Digite o nome do remédio: ")
    vezes = int(input('Quantas Vezes foi comprado: '))
#Adicionando no dicionario
    remedios[nomedoremedio] = vezes
#shallowcopy dos remedios
copia_remedios = remedios

#Iterando o shallowcopy
for nome, quantidade in copia_remedios.items():
    print(f"{nome}: {quantidade}")
