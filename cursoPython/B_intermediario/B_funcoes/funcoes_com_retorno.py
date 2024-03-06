"""
Funcoes com Retorno

Sao funcoes que retornam algum dado/elemento conforme oque voce define.
E para retornar usamos a palavra reservada "return"

OBS: palavra reservada sao palavras laranja, que nao pode ser variavel

OBS: Nao confunda return com o print, porque o return apenas traz de volta
o que foi pedido, ja o print apenas imprime.

OBS: Em python, quando uma funcao nao retorna nada, o retorno e None
"""


def dividir(num1, num2):
    return num1 / num2
# return fica so retorna a acao . if / for / while etc .
# ele so vai funcionar se tiver com o print em baixo


print(dividir(10, 5))
