"""
Funcoes com Docstrings

Docstring e a documentacao da funcao, ou seja, e a explicacao de como a
funcao funciona, passo a passo.

Recomendada quando temos uma funcao grande

OBS: Podemos pegar a documentacao de uma funcao usando  a propriedade
especial __doc__. ou usando a funcao help().
"""


def celular_info(marca, preco, data_de_fabricacao):
    """
    E uma funcao para imprimir as informacoes de um celular.

    :param marca: E a marca de um celular.   #param =  parametro
    :param preco: E o preco do celular.
    :param data_de_fabricacao: E a data de fabricacao.
    :return: E o retorno das informacoes
    """
    return f'Marca: {marca}, preco: R${preco}, data de fabricacao: {data_de_fabricacao}'


print(celular_info('Samsung', 1198.99, '13/04/2023'))
print(celular_info.__doc__)
print(help(celular_info))
#segurar ctrl e apertar no HELP

# Recomenda a do __doc__ para ser usado , dar preferencia