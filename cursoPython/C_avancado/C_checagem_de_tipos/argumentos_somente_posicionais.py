"""
Argumentos somente posicionais

/ — tudo que estiver antes da barra é considerado posicional. (nao pode mudar de posição)
* — tudo que estiver depois do asterisco é considerado obrigatório.(obrigatório , tem que ter)
"""


def add_imposto(valor, /):
    return valor + 12.5


print(add_imposto(10))


# Obrigando parâmetros
def add_imposto(*, valor):
    return valor + 12.5


print(add_imposto(valor=50))
