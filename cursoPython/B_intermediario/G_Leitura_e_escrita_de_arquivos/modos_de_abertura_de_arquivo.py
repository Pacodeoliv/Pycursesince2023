"""
Modos de abertura de arquivo

r -> leitura (padrao)
w -> escrita - sobrescreve caso o arquivo ja exista
x -> escrita - somente se o arquivo nao existir, se existir gera FileExistsError
a -> escrita - adciona o conteudo ao final do arquivo
+ -> modo de atualizacao : leitura e escrita (temos o controle do cursor)

OBS.: no modo 'a' (append), se o arquivo nao existir sera criado. Se existir, o novo conteudo SEMPRE vai ser
adicionado ao final do arquivo. Com o modo 'a'  nao controlamos o cursor.
"""

# Exemplo com 'x'
try:
    with open('filmes.txt', 'x') as arquivo:
        arquivo.write('Batman')
except FileExistsError:
    print('Arquivos ja existe.')

# Exemplo com 'a'
with open('dispositivos.txt', 'a') as arquivo:
    arquivo.write('teclado\n')
    # arquivo.seek(3)  - nao e possivel fazer a leitura do arquivo
    arquivo.write('tv')


# Exemplo com r+
with open('sorvetes.txt', 'r+') as arquivo:
    arquivo.write('chocolate\n')
    arquivo.write('baunilha')
    arquivo.seek(1)
    arquivo.read()
    print(arquivo.read())
