"""
Funcoes de Maior Grandeza - Higher Order Functions (HOF)

Quando uma linguagem de programacao suporta HOF, indica que podemos ter funcoes que
retornam outras funcoes como resultado ou ate mesmo podemos passar funcoes como
argumentos/parametros para outras funcoes.
"""


def msg():
    return 'msg'


def msg_completa(msg):
    print(f'A funcao usada e {msg}')


msg_completa(msg())