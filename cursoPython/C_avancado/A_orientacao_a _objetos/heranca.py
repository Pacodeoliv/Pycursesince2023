"""
Herança

É usado para fazer uma classe herdar comportamentos de outra classe.

Tudo que a classe pai tiver , a classe filho deve ter obrigaróriamente

Super

É usado para mostrar qualquer atributo da classe PY

"""

class Animal:                  # CLASSE PAI
    def __init__(self, tipo, idade):
        self.tipo = tipo
        self.idade = idade


    def mostrar_info(self):
        print(self.tipo)
        print(self.idade)


   # apertar no init e dar alt esq + enter
class Cachorro(Animal):             # CLASSE FILHO
    def __init__(self, tipo, idade, nome):
        super().__init__(tipo, idade)   # SUPER = acessa oque tem na classe pai
        self.nome = nome

    def mostrar_info(self):
        super().mostrar_info()
        print(self.nome)


cachorro = Cachorro('vira-lata', 5, 'Bob')
cachorro.mostrar_info()
