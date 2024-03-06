"""
Crie um numedtuple de filme que tenha como parametros o nome , o valor do ingresso e a data de estreia. a partir da
tupla , faca um desempacotamento e no final  itere a tupla

"""
from collections import namedtuple

filme  = namedtuple('filme','nome valor datadeestreia')

filmee = filme(nome='Os Incriveis', valor='15 Reais', datadeestreia='15 de Outubro 2023')

nome, valor, datadeestreia = filmee
print('=-' * 10)
print('nome: ', nome)
print('valor: ', valor)
print('Data de estreia: ', datadeestreia)

