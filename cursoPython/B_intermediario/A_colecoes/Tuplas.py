""""
Tuplas

As tuplas sao bem parecidas com listas. Mas tem duas diferencas:
- As tuplas sao feitas com parenteses ( )
- As tuplas sao imutaveis, ou seja, nao tem como mudar uma tupla depois que ela
foi criada.
"""

#Quando a tupla tiver letras por 'XXXX' entre eles
#As tuplas podem ser feitas de 2 maneiras:
tupla1 = (1, 22, 31, 45, 81)
tupla2 = 90, 12, 41, 71, 12
print(type(tupla1))
print(type(tupla2))

#Tuplas com 1 elemento
numeros1 = (3) # Isso NAO e uma tupla, mas na verdade um int
numeros2 = (3,) #Isso e uma tupla
numeros3 = 3, #Isso e uma tupla

# OBS: Tuplas sao definidas a partir das virgulas e nao pelos parenteses

# Desempacotamento de tuplas
professores = ('Gabriel', 'Anderson')
professor1, professor2 = professores

print(professor1)
print(professor2)

#Iterando sobre uma tupla
#Iterando = mexendo em aldo dentro
#basicamente pegar oque ta dentorcom for/while e editar isso
cores = ('vermelho', 'laranja', 'amarelo', 'roxo')

#para cada cor em cores
for cor in cores:
    print(cor)

# Slicing
# tupla[inicio:fim:passo/pulo]

#         0,   1,  2,  3,  4,  5
valores = 10, 41, 53, 79, 90, 100
print(valores[0:2]) # [0:1]
print(valores[0:6])
print(valores[0:])   #sem valor tambem vai ate o ultimo
print(valores[:6])   #do zero ate o final do indice
print(valores[:])   #do zero ate o final do indice
print(valores[1:4:2])

# OBS: O "fim" e sempre -1

# Indice e como e separado as posicoes de devido valor/ elemento

#Shift+F6 muda todos os valores (da a opcao de nos comentarios tambem)

# Fazendo uam copia

tupla = 30, 49, 84

imagem = tupla

print(tupla)
print(imagem)

""""
tupla = 30, 49, 84

copia = tupla

print(tupla)
print(copia)
"""
