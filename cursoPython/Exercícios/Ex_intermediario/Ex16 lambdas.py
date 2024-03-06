"""
Crie uma lambda para colocar 100 reais de taxa em produtos da China que tenha como parâmetros o produto e o preço dele,
e tenha como retorno uma mensagem trazendo o produto + o valor com 100 reais de taxa. No final use a lambda.
"""


somar = lambda item1, vlr: f'Item: {item1}, valor: {vlr + 100}'
print(somar('cadeira', 100))