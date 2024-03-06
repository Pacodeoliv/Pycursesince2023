"""
Map

com map, fazemos mapeamento de valores para funcao.
"""


def adicionar_imposto(valor):
    return valor + 24.5


print(adicionar_imposto(10))

print('-=' * 10)

valores = [98, 24, 56, 16]

# Map e uma funcao que recebe dois parametros: o primeiro a funcao e o segundo um
# iteravel. Retorna um map Object.
mapeando = map(adicionar_imposto, valores)
print(list(mapeando))
# List para colocar o mapeando em lista (tuple para fazer tupla)

"""
map() x filter()

map() - recebe dois aparametros, uma funcao e um iteravel e retorna um objeto mapeando a
funcao para cada elemento do iteravel.

filter() - recebe dois parametros, uma funcao e um iteravel e retorna um objeto filtrando apenas
os elementos de acordo com a funcao.
"""
