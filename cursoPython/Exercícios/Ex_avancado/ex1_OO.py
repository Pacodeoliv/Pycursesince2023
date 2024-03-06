"""
Crie uma classe Carro que:
1º Tenha um atributo de classe "data_lancamento";
2º Tenha um construtor com os atributos de instância "marca" e "valor" (valor precisa ser tratado como privado);

Depois disso:
1º Crie uma variável usando a classe e passando os atributos corretamente;
2º Imprima todos os atributos;
3º Crie um atributo dinâmico chamado "qnt_de_vendas" e o imprima.
"""


class Carro:
    data_lancamento = '22Dec23'

    def  __init__(self, marca, valor):
        self.marca = marca
        self.__valor = valor


carro = Carro ('Ferrari', 220000)
print(carro.marca)   # acessando marcas
print(carro._Carro__valor)  # acessando valor privado

print(Carro.data_lancamento)    # Acessando o atributo / classes

carro.qnt_de_vendas = 59
print(carro.qnt_de_vendas)
