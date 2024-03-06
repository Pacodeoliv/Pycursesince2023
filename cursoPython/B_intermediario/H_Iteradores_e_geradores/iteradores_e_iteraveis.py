"""
Iterators e Iterable

Iterator (iterador):
- Um objeto que pode ser iterado;
- Um objeto que retorna um dado, sendo um elemento por vez quando uma funcao next() e usada.

Iterable (iteravel):
- Um objeto que ira retornar um iterator quando a funcao iter() for usada/chamada.
"""

nome = 'Juliana'  # E um iterable

iter_nome = iter(nome)  # E um iterator

print(next(iter_nome))
print(next(iter_nome))
print(next(iter_nome))
print(list(iter_nome))

# next = separa um por vez