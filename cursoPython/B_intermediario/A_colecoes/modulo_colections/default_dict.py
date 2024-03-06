"""
Default Dict

Ao usar esse tipo de dicionario, temos que informar um valor default.
este valor sera utilizado sempre que nao houver um valor definido.
caso tentemos acessar uma chave que nao existe, essa chave sera criada
e o valor default sera atribuido

OBS: O DefaultDict sempre tem que estar com lambda
"""

from collections import defaultdict

cores = defaultdict(lambda: 'Cor nao definida')

print(cores[1])

cores[2] = 'Vermelho'
print(cores[2])

