"""
Dicionarios

Funcionam com chave e valor

OBS: Tem dois pontos importantes:
    - Chave e valor sao separados por dois pontos 'chave:valor'
    - Tanto chave quanto valor podem ser de qualquer tipo de dado (Str , numero ou etc)
"""

# Declarando/criando um dicionario
comidas_favoritas = {'Joao': 'sushi', 'Mariana': 'frango', 'Samuel': 'lasanha'}

# Acessando um elemento

# Forma 1
print(comidas_favoritas['Mariana'])

# Forma 2 -  Essa forma e usada para ter uma mensagem de erro personalizada
print(comidas_favoritas.get('Gabriel', 'Nome nao encontrado.'))
# Se nao tiver nada depois da virgula , ele vai escrever "none"


# Verificando se determinada chave esta no dicionario
# Se estiver no dicionario , vai imprimir True , se nao , False
print('joao' in comidas_favoritas)

# Adicionando um elemento
comidas_favoritas['Nathan'] = 'feijoada'
print(comidas_favoritas)

# Atualizando um elemento
# Por chave(Nathan) , so pode ter um valor
comidas_favoritas['Nathan'] = 'bife'
print(comidas_favoritas)

# Removendo um dado

# Forma 1
comidas_favoritas.pop('Nathan')
print(comidas_favoritas)

# Forma 2
del comidas_favoritas['Samuel']
print(comidas_favoritas)

# Os dicionarios tem Deep Copy e Shallow Copy

# Acessando partes do dicionario (Geralmente usado com for)
print(comidas_favoritas.keys()) # As chave (nomes)
print(comidas_favoritas.values()) # So os valores (agregados)
print(comidas_favoritas.items())  # Sao tudo

#dentro do values e keys temos listas
#dentro do items temos duas Tuplas dentro desse caso


# Iterando sobre dicionario / desempacotamento de dicionarios
# Para cada chave e valor em comidas_favoritas
for nome, comida in comidas_favoritas.items():
    print(f'O(a) {nome} gosta de {comida}.')

# Limpando um dicionario
comidas_favoritas.clear()
print(comidas_favoritas)

# Os dicionarios em Python sao conhecidos como "Mapas" em outras linguagens.
