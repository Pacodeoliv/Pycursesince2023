"""
crie um set de ferramentas usadas para consertar um carro, depois faca um deepcopy e apartir da copia adicione
dois elementos ,depois crie outro set da mesma ideia e apartir dos ultimos 2 sets gere um conjunto de valores
que estao em ambos sets e no final gere um conjunto de valores diferentes
"""

ferramentas = {'chave de fenda', 'chave de boca', 'macaco'}
copia = ferramentas.copy()
copia.add('martelo')
copia.add('chave L')
print(copia)
outrasferramentas = {'macaco', 'pomada'}

ambos = copia.intersection(outrasferramentas)
print(ambos)

diferentes = copia.difference(outrasferramentas)
print(diferentes)

