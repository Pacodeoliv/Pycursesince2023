"""
Duck Typing

O tipo ou a classe de um objeto é menos importante que os métodos que o definem,
ou seja, ao invés de checar a classe ou
tipo de dado, são checados os métodos ou atributos específicos.
"""


class Funcionario:
    def __len__(self):
        return 50


func = Funcionario()
print(len(func))