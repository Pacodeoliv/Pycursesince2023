"""
Deque

E uma lista de alta performance
(para listas com muitos itens/valores)
"""

from collections import deque

# Criando um deque
# alunos = deque('Maria') -> Dessa maneira vai fazer com que "Maria fique com as letras separadas.
alunos = deque()

# Adicionando elementos
alunos.append('Joao')
print(alunos)

alunos.appendleft('Jeferson')
print(alunos)

# Removendo elementos
print(alunos.pop()) # Remove e retorna o ultimo elemento
print(alunos)

print(alunos.popleft()) # Remove e retorna o primeiro elemento
print(alunos)
