"""
Geradores

Todos os geradores sao iterators.
OBS.: O contrario nao e verdadeiro, ou seja, nem todo iterator
e um generator.

Ponrtos importantes:
- Generators podem ser criados com funcoes geradoras;
- Funcoes geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com Expressoes Geradoras.

Diferencas entre funcoes e funcoes geradoras:

Funcoes:
- Utilizam return
- Retorna apenas uma vez
- Quando executada, retorna um valor

Generator Function:
- Utilizam yield
- Podem retornar varias vezes
- Quando executad, retorna um generator
"""


def contar_ate(limite):
    for num in range (limite):
        yield num

contagem = contar_ate(10)

print(next(contagem))
print(next(contagem))
print(next(contagem))
print(next(contagem))
print(next(contagem))

