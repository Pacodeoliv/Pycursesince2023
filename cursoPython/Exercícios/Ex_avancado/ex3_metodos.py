"""
Crie uma classe chamada Carro que:
1º Tenha um atributo de classe chamado "cpf_do_dono";
2º Tenha o construtor com os parâmetros "nome_do_dono" e "data_de_compra";
3º Tenha um método de instância chamado "alterar_data";
4º Tenha um método de classe chamado "imprimir_cpf";
5º Tenha um método estático informando quanto tempo o dono tem o carro;
6º No final use cada um deles.
"""

class Carro:
    cpf_do_dono = '198.398.908-10'

    def __init__(self, nome_do_dono, data_de_compra):
        self.nome_do_dono = nome_do_dono
        self.data_de_compra = data_de_compra


    def alterar_data(self, data_de_compra):
        print(self.data_de_compra)   # apresentando o antes de alterar
        self.data_de_compra = data_de_compra
        print(self.data_de_compra)   # apresentar o depois de alterar

 #4º Tenha um método de classe chamado "imprimir_cpf";
    @classmethod
    def imprimir_cpf(cls):
        print(f'Classe: {cls}')
        print(cls.cpf_do_dono)

#5º Tenha um método estático informando quanto tempo o dono tem o carro;
    @staticmethod
    def imprimir_tempo_de_uso(data_de_compra):
        ano_atual = 2024
        tempo_de_uso = ano_atual - data_de_compra
        print(f'O dono tem o carro há {tempo_de_uso} anos.')

# 6º No final use cada um deles.

ca = Carro( 'Gustavo', 2022)
ca.alterar_data(2010)
Carro.imprimir_cpf()
Carro.imprimir_tempo_de_uso(2010)
