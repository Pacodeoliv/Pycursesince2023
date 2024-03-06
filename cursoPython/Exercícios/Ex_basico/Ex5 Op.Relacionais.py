"""
Leia do usuario dois numeros de um sorteio e verifique se o segundo numero
e maior ou igual ao primeiro
"""

n1 = int(input('Em um sorteio foram sorteados dois numeros , sendo o primeiro : '))
n2 = int(input('E o segundo: '))

print(f'O segundo numero e maior que o primeiro? ')
print(f'- {n1 >= n2}')
