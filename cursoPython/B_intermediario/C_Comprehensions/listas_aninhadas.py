"""
Listas Aninhadas

Sao listas dentro de listas.

Como acessar os dados:
Para acessar precisamos usar dois pares de colchetes. O primeiro serve para
indicar de qual lista menor queremos acessar algum elemento e o segundo serve para indicar qual elemento
queremos pegar.
Exemplo:
alunos[1][2]

OBS: ele imprime um valor por linha

"""

lista_maior = [[10, 321, 12], [90, 93, 31], [784, 539, 3]]

# Acessando
print(lista_maior[0][2])
print(lista_maior[2][1])
print(lista_maior[1][0])

# Iterando com o loop for
for lista_menor in lista_maior:
    for valor in lista_menor:
        print(valor)