"""
Crie um dicionário de periféricos que tenha como chave o periférico e tenha como valor seu preço,
depois faça um dictionary comprehension que pegue cada um dos elementos adicionando 10 reais em cada
preço. No final imprima o dictionary comprehension.
"""

perifericos = {'Mouse': 250, 'Teclado': 300, 'Mousepad': 150}
dict_comp = {periferico: valor + 10 for periferico, valor in perifericos.items() }
print(dict_comp)