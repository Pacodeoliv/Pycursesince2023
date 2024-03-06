
"""
Crie uma função para adicionar juros em um preço de mouse que tenha como parâmetros mouse,
preço e juros. Dentro da função faça um docstring e retorne o valor com juros. No final
execute a função e imprima a documentação.
"""


def mouse_info(mouse, preco, juros):
    """
     E uma funcao para imprimir as informacoes de um celular.
    :param mouse: Eo mouse do usuario.   #param =  parametro
    :param preco: E o preco do mouse.
    :param juros: E o juros em cima do valor do mouse.
    :return: E o retorno das informacoes
    """
    return f'Mouse: {mouse}, Preco: R${preco}, Juros R$ {juros}, valor com Juros: R${preco + juros}'


print(mouse_info('Razer', 200, 20))
print(mouse_info.__doc__)
print(help(mouse_info))