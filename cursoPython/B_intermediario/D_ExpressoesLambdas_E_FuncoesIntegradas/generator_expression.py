"""
Generator Expression

Nos comprehensions vimos:
    - List Comprehension
    - Dictionary Comprehension
    - Set Comprehension

Mas não vimos um "Tuple Comprehension", porque na verdade ele se chama Generator Expression. Então todas as ideias
e fundamentos que vimos lá vão ser aplicados aqui também (afinal mesmo tendo um nome diferente ainda é um
comprehension).
"""

alunos = ['Carlos', 'Daniel', 'Camila', 'João']

nomes_com_c = (nome[0] == 'C' for nome in alunos)
# nome[0] (para filtrar a primeira letra do nome
print(tuple(nomes_com_c))

# OBS.: O Generator Expression tem uma perfomance muito melhor que os outros comprehensions, entao se puder escolher
# use-o no lugar dos outros. (para quando voce vai lidar com MUITOS elementos).