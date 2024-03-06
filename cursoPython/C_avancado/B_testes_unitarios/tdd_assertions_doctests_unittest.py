"""
TDD - Test-driven Development (Desenvolvimento Orientado a Testes)

Com TDD é usado estágios de desenvolvimento:
    - Você escreve seu teste primeiro;
    - E então escreve o código mínimo suficiente para fazer o teste
    passar, ou seja, executar com sucesso;
    - E por último refatora o código para realizar a funcionalidade e
    testa novamente.

Estes estágios são conhecidos como:
    - Red;
    - Green;
    - Refactor.
"""

# -----------------------------------------------------------------------------------------

"""
Assertions - Afirmações/Checagens/Questionamentos

Usamos a palavra reservada 'assert' para realizar simples afirmações
utilizadas nos testes, para assim checar se são válidas ou não. Se as
expressões forem verdadeiras, retornam None (null). E caso sejam falsas levanta
um erro chamado AssertionError.

OBS.: Nós podemos especificar um segundo argumento ou mesmo uma mensagem
de erro personalizada.

OBS.: O assert pode ser usado em qualquer parte do código, não precisa
apenas ser usado nos testes.

*ALERTA: Cuidado com assert, porque:
Se um programa Python for executado sem o parâmetro -O, nenhum assertion
será válido, ou seja, todas as suas validações já eram. Para colocar esse
parâmetro, precisamos executar pelo terminal, usando: -python -O 
programa.py
"""


def escolher_sorvete(sorvete):
    assert sorvete in [
        'chocolate',
        'baunilha',
        'coco',
        'menta'
    ], 'A opção precisa ser válida!'
    return f'O sorvete escolhido foi {sorvete}.'


sorvete = 'coco'
print(escolher_sorvete(sorvete))

print('-=' * 20)

# -----------------------------------------------------------------------------------------

"""
Doctests

São testes que colocamos na docstring das funções/métodos Python. (Ou seja , explicar)

Para rodar um teste do doctest:
python -m doctest -v nome_modulo.py
"""

'''
def somar(num1, num2):
    """
    Soma os números

    >>> somar(5, 10)
    15

    >>> somar(70, 2)
    79
    """
    return num1 + num2
'''

# -----------------------------------------------------------------------------------------

"""
Introdução ao módulo Unittest

Unittest -> Testes Unitários

O que é teste unitário?
É a forma de se testar unidades individuais do código fonte. Unidades
individuais podem ser: funções, métodos, classes, módulos, etc.

Para criar nossos testes, criamos classes que herdam do unittest.TestCase
e a partir de então ganhamos todos os assertions presentes no módulo.

Para rodar os testes, usamos unittest.main()

TestCase -> Casos de teste para a sua unidade

Conhecendo os assertions
https://docs.python.org/3/library/unittest.html

Por convenção, todos os testes em um TestCase devem ter o seu nome iniciado
com test_

Para executar os testes com unittest = python nome_do_modulo.py

Para executar os testes com unittest no modo verboso = python nome_do_modulo.py -v

Docstrings nos testes - podemos acrescentar (e é recomendado) docstrings em nossos
testes.
"""

'''
import unittest


def escolher_jogador(jogador):
    return f'O jogador escolhido foi {jogador}.'


class ClasseTeste(unittest.TestCase):
    def test_jogador_certo(self):
        """
        Testando o retorno com a escolha do jogador correto.
        :return: O jogador escolhido foi aspas.
        """

        self.assertEqual(
            escolher_jogador('nobru'), 'O jogador escolhido foi aspas.'
        )


if _name_ == '_main_':
    unittest.main()
'''

# -----------------------------------------------------------------------------------------

"""
Unittest - antes e após hooks

Hooks -> são os testes em si, ou seja, a execução dos testes.

setUp() -> antes de cada método de teste, é útil para criarmos
instâncias de objetos e outros dados.

tearDown() -> é executado ao final de cada método de teste. É útil
para excluir dados ou fechar conexões com banco de dados.

Sequência de execuções:
Dentro da classe, temos:
    - setUp() -> configurações do setUp();
    - test_seu_metodo() -> seu método em que o setUp() vai rodar antes do teste
    e o tearDown() vai rodar depois;
    - tearDown() -> configurações do tearDown().
"""

import unittest


class Computador:
    def __init__(self, marca, preco):
        self.marca = marca
        self.preco = preco

    def imprimir_info(self):
        print(self.marca)
        print(self.preco)


class ComputadorTestes(unittest.TestCase):
    def setUp(self):
        print('Executando setUp()')
        self.computador = Computador('Pichau', 3400)

    def test_imprimir_info(self):
        self.computador.imprimir_info()
        self.assertEqual(self.computador.preco, 3000)

    def tearDown(self):
        print('Executando tearDown()')


if __name__ == '__main__':
    unittest.main()
