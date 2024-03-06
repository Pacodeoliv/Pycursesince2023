"""
Bloco with

E usado para dar o close() automaticamente no streaming que foi aberto.
"""

with open('teste.txt') as arquivo:
    print(arquivo.read())
    print(arquivo.closed)

print(arquivo.closed)
