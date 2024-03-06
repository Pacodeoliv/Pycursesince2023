"""
Crie uma classe chamada Bolsa que tenha os atributos "marca"
e "preco", tenha um construtor e tenha o método mágico __repr__
(que tenha um print mostrando a marca e o preço da bolsa).
No final use a classe.
"""

class Bolsa:
    def __init__(self, marca, preco):
        self.marca = marca
        self.preco = preco

    def __repr__(self):
        return f'A minha bolsa é da {self.marca} , ela custou {self.preco}.'

bolsa = Bolsa('Lous Vitton', 30000)
print(bolsa.__repr__())
