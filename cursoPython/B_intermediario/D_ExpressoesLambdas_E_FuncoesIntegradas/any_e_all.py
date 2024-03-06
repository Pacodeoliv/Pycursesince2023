"""
any() e all()

any() - retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False.
all() - retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável estiver vazio.
"""

print(any([0, 1, 2]))
print(any([1, 2]))
print(any([]))

print(all([0, 1, 2]))
print(all([1, 2]))
print(all([]))