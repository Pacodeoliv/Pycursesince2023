"""
1. Leia do usuário o valor de um monitor e uma quantidade de vezes que ele quer rodar o For,
 dentro do For você vai fazer o valor + 10 a cada vez que rodar.
"""

"""
nao consigo fazer o valor que aumenta virar a variavel 
"""
vlr1 = float(input('O monitor custa: '))
vlr2 = int(input('Quantidade que vai rodar: '))
for vez in range (0, vlr2):
    vlr1 = vlr1 + 10
    #vlr1 += 10
    print(f"{vlr1}")