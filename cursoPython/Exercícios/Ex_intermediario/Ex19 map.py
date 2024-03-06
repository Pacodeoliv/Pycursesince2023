"""
Crie uma função aplicar_desconto que tenha como parâmetro um preço e retorne o preço - desconto
(vc define o desconto q quer dar). Depois crie uma tupla de preços de quadros,
 e a partir dessa tupla use o map. No final imprima o map.
"""

def aplicar_desconto (preco):
    return preco - 3

preco_quadros = (25, 10, 15, 20)

mapeando = map(aplicar_desconto, preco_quadros)
print(tuple(mapeando))



