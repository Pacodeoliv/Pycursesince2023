"""
2. Leia do usuário o valor de uma casa e uma quantidade de vezes que ele quer rodar o For,
 dentro do For você vai dar o desconto: valor - 10.000 a cada vez que rodar.
"""


vlr1 = float(input('Uma casa custa: '))
vlr2 = int(input('Quantidade de parcelas: '))
for i in range (0, vlr2):
    vlr1 = vlr1 -10000
    #vlr1 -= 10000
    print(f"{vlr1}")