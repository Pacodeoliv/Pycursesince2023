"""
Try / except / else / finally

Onde tratar o codigo?
Toda entrada (por exemplo: input) deve ser tratada!

Else -> e executado somente se nao ocorrer o erro.
Finally -> e sempre executado, independente do que aconteca.
"""

try:
    num_sorteio = int(input('Digite um numero para o sorteio:'))
except ValueError:
    print('Voce nao digitou o valor corretamente, tente novamente!')
else:
    print(f'O numero digitado foi {num_sorteio}')
finally:
    print('Finalizando o programa...')
