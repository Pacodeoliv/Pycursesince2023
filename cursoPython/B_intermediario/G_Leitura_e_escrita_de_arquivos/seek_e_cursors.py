"""
Seek e cursors

seek() -> e utilizada para movimentar o cursor pelo arquivo.
"""

arquivo = open('teste.txt')

print(arquivo.read())
arquivo.seek(3)
print(arquivo.read())

print('-=' * 20)

"""
OBS.: quando abrimos um arquivo com a funcao open() e criada uma conexao
que se chama streaming. Ao finalizar as tarefas com o arquivos devemos fechar essa 
conexao com a funcao close().

Passos para trabalhar arquivo:
1- Abrir o arquivo
2- Manipular
3- Fechar
"""

