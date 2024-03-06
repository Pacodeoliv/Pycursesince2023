"""
Sets (conjuntos)

Pontos importantes:
    - Nao possuem valores duplicados ;
    - Nao possuem valores ordenados;
    - Os elementos nao sao acessados via indice, ou seja, os conjuntos nao
    sao indexados.
    indexados = acessados por posicao (indice)
OBS: Os sets tambem podem ter elementos de varios tipos.
"""

# Declarando/ criando um set
idiomas = {'ingles', 'portugues', 'espanhol', ' frances'}
print(type(idiomas))

# Adicionando um elemento
idiomas.add('alemao')

print(idiomas)

# Removendo um elemento (OBS: Para remover precisamos colocar o elemento em
# si, e nao o indice dele)

# Forma 1
idiomas.remove('ingles')
print('idiomas')

# Forma 2 - Essa maneira nao mostra erros
idiomas.discard('chines')

# Os sets ou conjuntos tem Deep Copy e Shallow Copy

idiomas2 = {'mandarim', 'japones', 'russo', 'coreano'}

# Gerando um conjunto com valores unicos

# Forma 1 - Usando union
unicos1 = idiomas.union(idiomas2)
print(unicos1)

# Forma 2 - usando o caractere pipe |
unicos2= idiomas | idiomas2
print(unicos2)

# Gerando um conjunto de valores que estao em ambos os sets

# Forma 1 = usando intersection
ambos1 = idiomas.intersection(idiomas2)
print(ambos1)

# Forma 2 - usando o &
ambos2 = idiomas & idiomas2
print(ambos2)

# Gerando um conjunto de valores diferentes

diferentes1 = idiomas.difference(idiomas2)
print(diferentes1)

diferentes2 = idiomas2.difference(idiomas)
print(diferentes2)
