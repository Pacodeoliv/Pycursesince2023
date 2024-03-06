"""
Dictionary Comprehension

Tem a mesma ideia do List Comprehension, mas e para dicionario, ou seja, vamos mexer com chave e valor.

Sintaxe/Estrutura:
{chave: valor for chave, valor in iteravel}
"""

pessoas = {'Joao': 15,'Guilherme': 23, 'Julia': 47}

dict_comp = {nome: idade for nome, idade in pessoas.items()}
# dict_comp = {nome: idade +10 for nome, idade in pessoas.items()}
# pode ser usado da forma a cima

print(dict_comp)

funcionarios = {1500, 2300, 4400}
dict_comp2 = {salario: salario - 400 for salario in funcionarios}
print (dict_comp2)
