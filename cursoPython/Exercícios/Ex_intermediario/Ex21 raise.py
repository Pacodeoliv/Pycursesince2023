"""
Crie uma função para aplicar um juros a um preço de um produto que tenha
como parâmetros o produto e o valor dele. Dentro da função verifique se os
tipos dos parâmetros estão certos, se não estiverem use o raise para lançar
o TypeError, e caso dê tudo certo retorne uma mensagem com o produto e o
preço + R$15,00 de juros. No final use a função duas vezes, a primeira de
maneira correta e a segunda de maneira errada.
"""

def aplicar_juros(produto, valor):
    if type(produto) is not str:
        raise TypeError('O nome do produto precisa ser String')
    if type(valor) is not int:
        raise TypeError('O valor do produto precisa ser um numero inteiro')

    return f'O valor do {produto} mais o juros fica R$ {valor + 15} .'


print(aplicar_juros('Suco', 15))
print(aplicar_juros(23, 23))
