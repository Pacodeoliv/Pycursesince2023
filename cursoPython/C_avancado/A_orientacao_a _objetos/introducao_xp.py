"""
Orientacao a Objetos

O que e?
Pense na OO como a representacao da vida real no computador

POO (Programacao Orientada a Objetos)
OO ( orientacao a Objetos)

Classes:
Sao objetos.

Atributos:
Sao caracteristicas desses objetos.
-----------------------------------------------------------------------------------------------------------------------

Em Python, existem 3 tipos de atributos:

1 - Atributos de Instancia
Sao os atributos que contem informacoes que passamos ao usar a classe.

2 - Atributo de Classe
Sao os atributos que estao ligados com a classe.
** Pra programacao tudo e objeto

3 - Atributos Dinamicos
Sao os atributos de Instancia que podem ser criados em tempo de execucao, e como se fossem atributos de instancia
temporarios.

OBS.: em Python todo atributo de uma classe e publico, ou seja, pode ser acessado de qualquer lugar. Caso precisemos
informar que um atributo deve ser tratado como privado usamos __ ( duplo underline) antes do seu nome (isso e chamado
de Name MangLing).
------------------------------------------------------------------------------------------------------------------------

Construtores -> __init__
Como diz o proprio nome, sao usados para construir o objeto.

OBS.: construtores podem ter parametros, com eles explicamos o que e necessario para construir um objeto.
"""

class Pessoa:
    cargo = 'desempregada'

    def __init__(self, nome, idade):
        self.nome = nome
        self.__idade = idade  # Name MangLing
# self significa o objeto em si (ele cria um espaco na memoria do computador um espaco pro produto *nome*
"""
qual a difrerenca do self.nome pro nome sem self?
- o sem self se refere aos nome que a pessoa passar 
"joao" em baixo


Em python nada e privado , quando dizemos que o atributo e privado em Python a pessoa
deve tratar aquilo como privado , mas da pra ser acessado


def __init__(self, atributo1):
    self.atributo1 = atributo1
"""

pessoa = Pessoa('João', 22)  # Atributos de Instância - eles são os "nome" e "idade" no construtor.
print(pessoa.nome)
print(pessoa._Pessoa__idade)  # Acessando um atributo privado (forma possível, mas não recomendada)
# variavel._Classe__atributo
#só consigo acessar com a classe , porque é um atributo de classe


print(Pessoa.cargo)  # Para atributos de classe , acessamos a partir da classe
# Classe.atributo

pessoa.email = 'joao@gmail.com'  # Atributo dinâmico (literalmente criado so para aquele momento , algo bem temporario)
print(pessoa.email)
