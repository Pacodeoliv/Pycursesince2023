"""
Crie uma lista de marcas de carro e depois faça um Generator Expression que verifique se a segunda letra
é a letra "A". No final imprima.
"""

marcas = ['Porshe', 'Ferrari', 'Chevrolet', 'Fiat', 'Mercedes', 'Audi']

nome_com_a = (nome[1] == 'A' for nome in marcas)

print(tuple(nome_com_a))
