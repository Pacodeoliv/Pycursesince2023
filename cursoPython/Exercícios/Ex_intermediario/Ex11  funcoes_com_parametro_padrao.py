"""
Crie uma funcao para imprimir instrumentos e tenha como parametros padroes 2 instrumentos , dentro da funcao
retorne os instrumentos . no final execute a funcao
"""

# valores reservas sao os do bloco da funcao
def imprimir(ins1 = 'violino' , ins2 = 'sax soprano'):
    return (f'Eu toco {ins1} e meu melhor amigo costuma tocar {ins2}')

# passagem de valores
print(imprimir('Viola', 'Chello'))
print(imprimir('Tuba'))
print(imprimir())
