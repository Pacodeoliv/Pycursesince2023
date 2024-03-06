"""
Funcoes

Sao usadas para fazer tarefas especificas e repetitivas.

OBS: Se voce escrever uma funcao que realiza varias tarefas
dentro dela, e melhor fazer uma "separacao de tarefas" em varias
funcoes.

DRY - Don't Repeat Yourself = Conceito utilizado para evitar codigo
repetido.

Definindo funcoes:
def nome_da_funcao():
    bloco_da_funcao

OBS: Antes da funcao e depois dela sempre teremos 2 linhas em branco
por causa do PEP-8 (que e, basicemente, um acordo para deixar o codigo
mais bonito)
"""


# Criando funcao
def imprimir_mensagem():
    print('Mensagem personalizada')


# usando a funcao
imprimir_mensagem()  # quando poem parenteses o codigo entende que vai ser pra rodar

# Em Python, podemos criar variaveis para uma funcao (isso nao e comum)
msg = imprimir_mensagem
msg()  # Usando/chamando a funcao

# ctrl + F = pesquisar no codigo
