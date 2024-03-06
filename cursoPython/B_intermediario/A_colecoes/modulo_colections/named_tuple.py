"""
Named Tuple

E uma tupla que informamos um nome e parametros, ou seja, e uma tupla
explicita.
"""

from collections import namedtuple

# Existem 3 formas de criar/declarar um namedtuple

                    # Nome       # Parametros
animal1 = namedtuple('animal', 'nome tipo idade')
animal2 = namedtuple('animal', 'nome, tipo, idade')
animal3 = namedtuple('animal', ['nome', 'tipo', 'idade'])

# Usando

bob = animal1(nome='Cachorro', tipo='Terrestre', idade='5 anos')
print(bob)

# Acessando os dados

# Forma 1
print(bob.nome)
print(bob.tipo)
print(bob.idade)

# Forma 2
print(bob[0])  # nome
print(bob[1])  # tipo
print(bob[2])  # idade

print(bob.count('Cachorro'))
print(bob.index('Cachorro'))
