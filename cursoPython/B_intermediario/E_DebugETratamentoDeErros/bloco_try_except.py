"""
O bloco try/except

Usamos esse bloco para tratar erros que podem acontecer no codigo.
Prevenindo que o programa pare de funcionar ou que o usuario receba
mensagens de erro inesperadas.

Sintaxe/estrutura:
try:
    codigo que pode dar errado
except:
    o que fazer se der errado
"""
# Tratar erro = tentar arrumar o erro

def somar(num1, num2):
    try:
        return num1 + num2
    except TypeError:
        return ' voce passou algum valor de maneira errada. Tente novamente!'


print(somar(10, 40))
print(somar(80, '90'))
