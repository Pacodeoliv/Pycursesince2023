"""
Modulo Collections

Collections -> High-perfomance Container Datatypes

Counter -> Recebe um iteravel como parametro e cria um objeto do tipo
Collections Counter que e parecido com um dicionario, contendo como chave
o elemento da lista passada e como valor a quantidade de ocorrencias
desse elemento.

OBS: Para usar qualquer collection precisamos fazer sempre o import.

iteravel : aquilo que pode ser manipulado ou alterado

OBS: import sempre tem de vir na priemira linha

"""

from collections import Counter

precos_camisetas = [90.81, 29.10, 90.81, 45.3, 29.10]
counter = Counter(precos_camisetas)
print(counter)

