"""
Crie uma funcao para definir pratos favoritos de uma pessoa que tenha como parametros o nome da pessoa e um kwargs
com cada prato ou sobremesa favoritos e tambem retorne uma mensagem, no final use a funcao
"""


def pratos_favoritos(pessoa, **pratos):
    return f'A {pessoa} ama comer , suas comidas favoritas sao {pratos} .'


print(pratos_favoritos('Maria', prato='Feijao tropeiro ', sobremesa='Torta Holandesa '))
