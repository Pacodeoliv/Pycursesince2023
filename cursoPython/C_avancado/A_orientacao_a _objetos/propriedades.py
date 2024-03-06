"""
Propriedades / Getters e Setters

getter - pega o atributo
setter - altera o atributo

 props - atalho getter e setter 
 prop - atalho getter 


 ***usamos getter e setter principalmente pra evitar conflito no codigo
 ***qando precisarmos acessar um valor dentro de uma classe , sempre usar GETTER E SETTER
 *** getter e setter sao melhores para ifs
 
"""


class Computador:
    def __init__(self, marca, valor):
        self._marca = marca
        self._valor = valor

    @property
    def marca(self):     # getter
        return self._marca

    @marca.setter   # setter
    def marca(self, value):
        self._marca = value

    @property
    def valor(self):  # getter
        return self._valor

    @valor.setter
    def valor(self, value):  # setter
        self._valor = value


comp = Computador ('Lenovo', 1600)
comp.marca = 'Samsung'
comp.valor = 1800
print(comp.marca)
print(comp.valor)

