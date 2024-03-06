"""
crie um deque de materiais escolares e adicione tres materiais  , depois itere sobre esse deck e depois faca um
desempacotamento , depois de tudo isso faca um deep copy e apartir da copia remova o primeiro elemento. no final
acesse o segundo elemento que restou da copia
"""

from collections import deque

# criando o deque
materiais = deque()

# adicionando os materiais
materiais.appendleft('Cimento')
materiais.append('areia')
materiais.append('pincel')
materiais.append('tijolo')

# iterando
for material in materiais:
    print(f'Materiais: {material}')

# desempacotamento
mat1, mat2, mat3, mat4 = materiais

# Desempacotando
print(f'segue lista de desempacotamento: 1 - {mat1}, 2-{mat2}, 3-{mat3}, 4-{mat4} ')

# Criando deepcopy
copi = materiais.copy()

# Imprimindo copia
print(copi, ' essa e a copia')

# Removendo primeiro elemento
print(copi.popleft())
print(copi)
