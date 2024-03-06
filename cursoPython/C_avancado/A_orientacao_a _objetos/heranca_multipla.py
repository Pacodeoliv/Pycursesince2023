"""
Herança Múltipla

É quando uma classe herda de várias outras.
"""


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Desenvolvedor:
    def __init__(self, linguagem_programacao, experiencia):
        self.linguagem_programacao = linguagem_programacao
        self.experiencia = experiencia


class Funcionario(Pessoa, Desenvolvedor):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)


funcionario = Funcionario ( 'João', 27)
