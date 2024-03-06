"""
Métodos

São iguais a funções, só que para classes.

Em python, temos 3 tipos:

1 - Metodos de Instância = têm acesso à instância do objeto
2 - Métodos de Classe = têm acesso à Classe
3 - Métodos Estáticos = não têm acesso a nenhum dos dois, ou seja,
fazem tarefas diferentes.


Instância = valores que eu passo , as caracteristicas



pra que o python entenda que é um método de classe , é obrigatório o uso do
 -> @classmethod

cls = class (usamos ele pra acessar o atributo da classe)

"""


class Celular:
    data_lancamento = '20/09/2022'   # cls pega isso aqui

    def __init__(self, marca, valor):
        self.marca = marca
        self.valor = valor

    # Método de instância
    def alterar_valor(self, valor):
       # print(self.valor)
        self.valor = valor
       # print(self.valor)

    # Método de classe
    @classmethod  # anotação
    def acessar_data(cls):
        print(f'Classe: {cls}')
        print(cls.data_lancamento)

    # Método Estático
    @staticmethod
    def imprimir_info():  # especificar
        print('O celular é vendido na cor preta.')

        # nesse caso especificamos que o celular é da cor preta


ce = Celular('Samsung', 1500)
ce.alterar_valor(1700)
Celular.acessar_data()
Celular.imprimir_info()

# metodos de classe só podem ser acessados pela classe .
# exemplos a cima


"""
Basicamente se esta fora da classe é uma função , se ta dentro é um metodo
é a mesma coisa , não muda muita coisa
"""



# Oque é um construtor ??
# __init__  kkkkk