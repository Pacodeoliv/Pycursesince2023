"""
Decoradores (decorators)

Como diz o proprio nome, sao usados para decorar o codigo, mas nao apenas para uma questao de esteticas, e sim
para uma questao de produtividade.
"""


# Decorador com Syntact Sugar ( Acucar Sintatico)
def cumprimentar(funcao):
    print('Ola')
    return funcao


@cumprimentar
def se_apresentar(nome):
    print(f'prazer em te conhecer, me chamo {nome}')


se_apresentar('Gustavo')