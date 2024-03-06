"""
Declare um dicionario de produtos que tenha como chave  o produto e tenha como valor o preco dele , depois faca um
Deep Copy e a partir da copia acesse o 3 elemento , adicione um elemento , remova o primeiro elemento , atualize o
segundo elemento e por ultimo itere sobre o dicionario
"""

produtos = {'vassoura': 10, 'caneta': 2, 'lapis': 1, 'borracha': 3}
copia = produtos.copy()
print(copia['lapis'])
copia['apontador'] = 4
print(copia)
del copia['vassoura']
print(copia)
copia['lapis'] = 1.5
for produto, preco in copia.items():
    print(f'O produto {produto} vale {preco}.')