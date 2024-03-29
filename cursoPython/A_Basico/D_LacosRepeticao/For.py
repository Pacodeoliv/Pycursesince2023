"""
Lacos de Repeticao - For

O For e usado para acoes repetitivas , ou seja, quando voce precisa
fazer algo muitas vezes voce pode usar o for.

*NO range do for temos 3 opcoes :
1 Colocar o numero do inicio e do final. Ex.: (1, 10)
2 Colocar apenas o numero do final. Ex.: (10) #sempre comeca do 0
3 Colocar o numero do inicio e do final e tambem o numero de passos. Ex.: (1, 10(ate o 9), 2)

*OBS: O final do For e SEMPRE -1

Estrutura:
para cada variavel no alcance (numero1, numero2)
for variavel in range(numero1, numero2)

continue: ignora tudo que tem abaixo e volta para a primeira linha do for.
"""

#FOr = para cada   (na leitura)



#para cada variavel no alcance(0, 9):
for numero in range(0, 10):
    print(numero)

print("-=" * 10)

"""
print(cliente1)
print(cliente2)

for cliente in range(0, 10:
    print(cliente)
"""

for numero in range(10):
    print(numero)
#o phyton sabe que tem que comecar do 0 , entao vai comecar sozinho

print("-=" * 10)

for numero in range(0, 10, 2):
    print(numero)
#ele vai pular de acordo com o 3 numero

#for numero in range(1, 10,):
#for numero in range(10):
#for numero in range(1, 10, 2):

print("-=" * 10)

for numero in range(0, 10, 2):
    if numero == 5:
        continue
    print(numero)
#ele ignora oque tem a baixo e volta pra primeira linha

print("-=" * 10)

vlr1 = float(input('O monitor custa: '))
vlr2 = int(input('Quantidade que vai rodar: '))
for i in range (0, vlr2):
    vlr1 = vlr1 + 10
    print(f"{vlr1}")