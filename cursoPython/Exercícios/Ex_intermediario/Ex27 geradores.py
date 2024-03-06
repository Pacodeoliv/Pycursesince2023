"""
Crie uma função geradora chamada "contagem_regressiva" que tenha como parâmetro limite,
e dentro dela faça um for que vá do limite até o zero, retornando cada número.
No final imprima usando next().
"""


def contagem_regressiva(limite):
    for num in range(limite, 0, -1):
        yield num


contagem = contagem_regressiva(5)

print(next(contagem))
print(next(contagem))
print(next(contagem))
print(next(contagem))
print(next(contagem))


