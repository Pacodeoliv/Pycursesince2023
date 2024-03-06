"""
Funcoes com Parametro Padrao (Default Parameters)

Sao funcoes que fazem com que os parametros tenham valores reservas.
E a passagem de valores e opcional.

resumindo , quando voce coloca , nao e obrigado passar valores

quando usar?
-geralmente numa ocasiao aonde precise de valores , mas a funcao so roda com
todos os valores. usa-se .
Resumindo , quando realmente precisa
"""

# valores reservas sao os do bloco da funcao
def multiplicar(num1=10, num2=2):
    return num1 * num2

# passagem de valores
print(multiplicar(30, 40))
print(multiplicar(20))
print(multiplicar())
