"""
Crie uma classe pai chamada "Carro" que tenha os atributos "marca" e "preco", tenha um construtor e tenha o método
"adicionar_juros" (que tem um parâmetro "juros" que vai adicionar dependendo do vendedor).

Crie uma classe filha chamada Fiat que herde de Carro e altere apenas o comportamento do método "adicionar_juros"
 (coloque o juros com um valor de R$200).

No final use a classe filha.
"""

class Carro:
    def __init__(self, marca, preco):
        self.marca = marca
        self.preco = preco


    # Função pai com fnução do juros
    def adicionar_juros(self, juros):
        self.preco += juros




# Crie uma classe filha chamada Fiat que herde de Carro e altere apenas o comportamento do método "adicionar_juros"
#  (coloque o juros com um valor de R$200).

class Fiat(Carro):
    def __init__(self, preco):
        super().__init__("Fiat", preco)


    # Classe Filho , tirei o juros de dentro do self, porque nao tem necessidade ja que adiciona o valor de juros
    # Manual em baixo

    def adicionar_juros(self):

        # muda o valor do juros manual na função pra definir o valor do juros no print (pois ja esta na função)
        self.preco += 200
        print(f'O valor do preço com juros é {self.preco}')


fiat = Fiat(1200)
fiat.adicionar_juros()
