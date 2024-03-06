"""
Crie uma funcao para imprimir a  media de notas que tenha como parametros 3 notas
"""

n1 = int(input('Escreva um valor: '))
n2 = int(input('Escreva um valor: '))
n3 = int(input('Escreva um valor: '))


def media_msg(n1, n2, n3):
    print(f'A media dos tres valores sao:{(n1 + n2 + n3) / 3} ')


media_msg(n1, n2, n3)

