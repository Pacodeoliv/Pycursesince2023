"""
sorted()

Como diz o proprio nome, o sorted() serve para ordenar. E podemos usa-los com qualquer iteravel.

OBS.: Nao confunda com a funcao sort() que tem em listas, porque ele so funciona em listas.
OBS. 2: O sorted() SEMPRE retorna uma lista com os elementos do iteravel ordenados.

"""

numeros = {9, 4, 6, 1}
print(sorted(numeros))

# Podemos tambem ordenar ao contrario
print(sorted(numeros, reverse=True))
