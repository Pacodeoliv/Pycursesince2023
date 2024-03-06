"""
Funcoes Aninhadas

Sao funcoes dentro de funcoes, tambem podem ser conhecidas como Nested Functions
"""

"""
def valor_sorvete(sabor, valor):
    if sabor == 'chocolate':
        def imposto():
            return valor + 5
        imposto()
    return f'sabro: {sabor}, valor: R${valor}'
"""

def valor_sorvete(sabor, valor):
    def imposto():
            return valor + 5
    return imposto()

print(valor_sorvete('chocolate', 3))

