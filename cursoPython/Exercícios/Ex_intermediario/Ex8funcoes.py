"""
Crie uma função para dar desconto em um preço, que tenha como parâmetros preço
original e desconto, no final use a função
"""

# Receba do usuario
preco1 = float(input('digite o preco: '))   # sempre usar o Float caso ele queira valor quebrado "70,5 %"
desconto1 = float(input('Digite o valor do desconto: '))   # sempre usar o Float caso ele queira valor quebrado "70,5 %"

"""
preco1 = int(input('digite o preco: '))
desconto1 = int(input('Digite o valor do desconto: '))

PS: evitar
"""

# Bloco da funcao
def desconto(preco1, desconto1):
    valordesconto = preco1 * (desconto1 / 100)
    precocdesconto = preco1 - valordesconto
    print(f'Preco com desconto: {precocdesconto}')

# Executar da funcao
precocomdescontofuncao = desconto(preco1 ,desconto1)
