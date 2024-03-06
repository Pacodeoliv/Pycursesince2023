"""
Ordered Dict

E um dicionario que garante a ordem de insercao dos elementos

OBS: Em um dicionario normal essa ordem *nao* e garantida.
"""

from collections import OrderedDict

perifericos = OrderedDict({'mouse': 120, 'teclado': 300, 'monitor': 1000})

for chave, valor in perifericos.items():
    print(f'chave: {chave}, valor: {valor}')

print('-=' * 10)

# Entendendo a diferenca entre o dicionario normal e Ordered Dict

# Dicionarios Comuns
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)  # True -> ja que a ordem dos elementos nao importa para
# o dicionario normal

# Ordered Dict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2)  # False -> ja que a ordem dos elementos importa para
# o Ordered Dict
