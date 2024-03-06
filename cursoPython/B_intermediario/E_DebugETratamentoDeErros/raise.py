"""
Levantando erros com raise

raise - lanca excecoes/erros

OBS.: o raise nao e uma funcao, e apenas uma palavra reservada

Para simplificar:
Pense no raise para criar as nossas proprias excecoes e mensagens de
erros.

Sintaxe/estrutura:
raise TipoDoErro('Mensagem de Erro')
"""


def funcionario_info(nome, idade):
    if type(nome) is not str:
        raise TypeError(' O nome do funcionario precisa ser uma string')
    if type(idade) is not int:
        raise TypeError('A idade do funcionario precisa ser um numero inteiro')
    return f'As informacoes do funcionario ficam: nome - {nome} e idade - {idade}'


print(funcionario_info('Joao', 22))
print(funcionario_info('Jessica', 'Dezoito'))
