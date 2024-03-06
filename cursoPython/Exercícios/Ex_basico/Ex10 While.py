"""
Receba do usuário um valor de uma camiseta e quantas vezes ele quer rodar o while,
 dentro do while você vai calcular camiseta + 10 até chegar ao limite digitado.
"""
cms1 = float(input('Essa camiseta vale: '))
vz1 = int(input('Numero de camisetas: '))

cont = 0
while cont < vz1:
    cms1 += 10
    cont += 1
print(f'Essa camiseta vale: {cms1}')

