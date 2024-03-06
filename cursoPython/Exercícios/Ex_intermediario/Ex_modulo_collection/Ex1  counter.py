"""
Receba do usuario 5 instrumentos (pode ser repetido ou nao ) e coloque os 5 dentro de uma lista , no final use o counter

"""


from collections import Counter

instrumentos = []

for i in range(5):
    ins = input("Digite um instrumento: ")
    instrumentos.append(ins)


contador = Counter(instrumentos)

print(contador)


