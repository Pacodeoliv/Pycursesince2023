"""
Set Comprehension

A mesma coisa que List Comprehension, mas para sets.

Sintaxe/Estrutura:
{valor for valor in iteravel}
"""

valores = {40, 51, 22}

set_comp = {valor * 2 for valor in valores}  #sets nao tem ordem , as posicoes vao ser aleatorias
print(set_comp)
