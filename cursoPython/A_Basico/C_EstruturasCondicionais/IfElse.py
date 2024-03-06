"""
Esttruturas Condicionais

if - se (A primeira condicao)
elif - senao se (A condicao intermediario)
else - senao  (A ultima condicao)

Usados para montar condicoes ao codigo
"""

# Identacao = 4 espacos antes da sentenca (TAB faz 4 espacos SHIFT+TAB vai pra tras)
# Obrigatorio os : para aplicar a regra

valor1 = 52
valor2 = 60

if valor1 > valor2:
    print('O primeiro valor e maior que o segundo.')
elif valor1 == valor2:
    print('Os valores sao iguais.')
else:
    print('O primeiro valor e menor que o segundo.')


# None = nulo