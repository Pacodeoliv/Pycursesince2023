"""
Escrevendo em arquivos

Para escrever usamos a funcao write()

Modos de abertura de arquivo:
https://docs.python.org/3/library/functions.html#open

Para escrita, podemos abrir o arquivo como 'w'. Se o arquivo nao existir, sera criado. caso ja exista, o anterior
sera apagado e um novo sera criado, ou seja, todo o conteudo anterior e perdido.

OBS.: ao abrir um arquivo para leitura, nao podemos escrever nele, mas apenas ler. O contrario tambem e assim.
Isso significa que quando abrimos o arquivo em algum modo e para ser manipulado daquela maneira.
"""

with open('frutas.txt', 'w') as arquivo:
    arquivo.write('Laranja\n')
    arquivo.write('Maca\n')
    arquivo.write('Pera')


"""
\n  vai fazer a escrita pular uma linha , tipo "enter"
"""

