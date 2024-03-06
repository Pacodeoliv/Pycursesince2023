"""
1 - Crie uma classe pai chamada "Pessoa" que tenha um construtor com os parâmetros "nome" e "idade".
2 - Crie uma classe filha chamada "Funcionario" que herde de "Pessoa" e tenha um construtor com um atributo novo chamado "cargo".
3 - No final use a classe filha.
"""

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_info(self):
        print(self.idade)
        print(self.nome)


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade)
        self.cargo = cargo

    def mostrar_info(self):
        super().mostrar_info()
        print(self.cargo)


pessoa = Funcionario( 'Carlos',28, 'Dev back end')
pessoa.mostrar_info()
