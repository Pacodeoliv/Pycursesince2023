"""
Leitura de arquivos

Para ter acesso ao que tem dentro de um arquivo usamos a funcao open()

https://docs.python.org/3/librabry/functions.html#open

OBS.: por padrao open() abre o arquivo para leitura. Se o arquivo nao existir
dara o erro FileNotFoundError
"""

arquivo = open('teste.txt')

leitura = arquivo.read()
print(leitura)
