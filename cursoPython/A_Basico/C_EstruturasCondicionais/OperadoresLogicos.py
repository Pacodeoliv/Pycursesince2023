"""
Operadores Logicos

Sao operadores usados para fazer comparacoes em "concordancia".

and = true and true ( Os dois devem ser verdadeiros)
or = True or True, True or False, False or True (pelo menos um tem que ser verdadeiro)
is = is True , is False (pra verificar se realmente e aquilo)
not = not True(False), not False(True) (sempre da o sentido contrario)
"""


num1 = 155
num2 = 221

if num1 > 150 and num2 > 150:
    print('Os dois numeros sao maiores que 150.')


valor1 = 59
valor2 = 96

if valor1 > 150 and valor2 > 150:
    print('Pelo menos um dos valores e maior que 70')

modo_claro = True

if modo_claro is True:
    print('O modo claro esta ativado')

if not  modo_claro:
    print('Modo claro ativado')