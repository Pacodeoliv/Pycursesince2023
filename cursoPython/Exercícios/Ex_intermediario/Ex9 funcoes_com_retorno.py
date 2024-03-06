"""
Crie uma função para mostrar a cor preferia de alguém que tenha como
 parâmetros nome e cor_favorita, depois retorne o nome + a cor.
 No final execute/rode a função.
"""

# Bloco da funcao
def corfavorita(nome, corfav):
    mensagem = f"{nome} prefere a cor {corfav}."
    return mensagem

# receba do usuario do problema
nome = input("Digite o nome da pessoa: ")
corfav2 = input("Digite a cor favorita da pessoa: ")

# Execucao da funcao
resultado = corfavorita(nome, corfav2)

# Print da funcao (aondeo return acompanha)
print(resultado)
