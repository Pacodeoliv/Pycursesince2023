"""
Crie uma classe Funcionario que:
1º Tenha um atributo de classe "cargo";
2º Tenha um construtor com os atributos de instância "nome" e "idade" (idade precisa ser tratada como privada);

Depois disso:
1º Crie uma variável usando a classe e passando os atributos corretamente;
2º Imprima todos os atributos;
3º Crie um atributo dinâmico chamado "tempo_na_empresa" e o imprima.
"""

class Funcionario:
    cargo = 'ajudante'

    def __init__(self,nome,idade):
        self.nome = nome
        self._idade = idade

cargo = Funcionario ('Leticia', 18)
print(cargo.nome)
print(cargo._idade)
cargo.tempo_na_empresa = '2 Anos'
print(cargo.tempo_na_empresa)
