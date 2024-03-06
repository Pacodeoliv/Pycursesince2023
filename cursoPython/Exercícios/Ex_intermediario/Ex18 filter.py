"""
Crie uma tupla de preços de sorvetes de uma sorveteria e filtre os preços que são maiores ou iguais a 10
e no final imprima esses preços como sendo preços caros.
"""


import statistics

Sorvetes = (2.5, 5, 8, 10, 12, 15)

valor1 = 10

maiores_igual = filter(lambda valor: valor >= valor1, Sorvetes)

print(list(maiores_igual))


