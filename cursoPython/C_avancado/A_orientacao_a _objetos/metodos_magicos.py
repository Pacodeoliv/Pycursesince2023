"""
Métodos Mágicos

São todos os métodos que têm dunder.

dunder = double underscore (dois underlines)

__repr__
é basicamente um metodo de representação de objetos

"""


class Filme:
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao

    def __repr__(self):
        return f'{self.nome} tem a duração de {self.duracao} minutos.'


filme = Filme('Titanic', 230)
print(filme.__repr__())
