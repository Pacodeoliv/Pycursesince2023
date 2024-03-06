"""
Lambdas

Sao funcoes sem nome, ou seja, funcoes anonimas. Serve para fazer as mesmas coisas que funcoes basicas, mas
de maneira mais resumida.

Sintaxe:
Lambda parametros: retorno
"""

# Funcao
def somar(num1, num2):
    return num1 + num2



# Lambda
calcular = lambda num1, num2: num2 + num2

# Usando os dois
print(somar(10, 44))
print(calcular(10, 44))
