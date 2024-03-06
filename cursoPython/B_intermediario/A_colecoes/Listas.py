"""
Colecoes sao usadas para guardar valores.

Listas

Pensa na lista como se fosse uma caixa de papelao (um bau), ou seja, voce
guarda o que quiser dentro e depois pode tirar para usar.

OBS: As listas usam colchetes []

OBS: As colecoes sempre comecam com indice 0, ou seja, as posicoes dos
elementos vao do 0 ate o ultimo elementos.

indice = posicao

"""

# Criando uma lista
marcas = ['Nike', 'Adidas', 'Fila']
print(marcas)

# Acessando um elemento da lista
print(marcas[1])

# Adicionando um valor dentro da lista
marcas.append('Puma')
print(marcas)

# Removendo um valor da lista
# marcas.pop() - o pop () vazio remove sempre o ultimo elemento
marcas.pop(2)
print(marcas)

# Removendo todos os elementos (zerados a lista)
marcas.clear()
print(marcas)

# Iterando sobre a Lista
# Iterar = ver oque tem dentro , fazer um check
# para cada marca em marcas:
for marca in marcas:
    print(f' Marca: {marca}')

# Desempacotamento de listas
# Dividir as listas
ingressos = [11.2, 90.1, 179]
ingresso1, ingresso2, ingresso3 = ingressos
print(ingresso1)
print(ingresso2)
print(ingresso3)

# Fazendo uma copia de uma lista

#Shallow Copy - cria uma ligacao entre a lista e a copia
# ele mexe com objetos em comum entre listas
idades = [18, 25, 67]
copia = idades

copia.append(30)

print(idades)
print(copia)

# Deep Copy
#o .copy em frente e o crucial para ser "deep copy" , ele mexe apenas em uma

idades = [90, 12, 16]
copia = idades.copy()

copia.append(51)

print(idades)
print(copia)
