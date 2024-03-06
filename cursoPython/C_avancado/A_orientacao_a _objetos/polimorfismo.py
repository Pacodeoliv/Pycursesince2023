"""
Polimorfismo

É a sobrescrita de métodos para mudar o comportamento do método
da classe pai.

override = nome tecnico em ingles
"""


class TV:
    def __init__(self, marca, preco):
        self.marca = marca
        self.preco = preco

    @staticmethod
    def info_extra(info):
        print(f'As informações extras da TV são: {info}')


class Samsung(TV):
    def __init__(self, preco):
        super().__init__('Samsung', preco)

    @staticmethod
    def info_extra(info):
        print(f'As informações da TV Samsung são {info}.')


samsung = Samsung(1800)
samsung.info_extra('A cor dela é vermelha')
