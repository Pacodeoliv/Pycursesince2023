"""
Crie uma função para dar desconto em um produto, que tenha como parâmetros o produto, valor e desconto.
Dentro da função use o bloco try/except, no try: tente retornar uma mensagem contendo o produto e o valor - desconto,
no except traga uma mensagem de erro para TypeError. No final use a função de maneiras correta e errada.
"""

def desconto(vlr1,vlr2):
    try:
        valor_com_desconto = vlr1 - vlr2
        return f"Esse e o valor do produto com desconto: {valor_com_desconto}"
    except TypeError:
        return 'O valor inserido esta incorreto , tente novamente '

print(desconto(10,2))
print(desconto(10,'2'))