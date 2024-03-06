"""
Modulos

Sao os proprios arquivos Python.

Existem duas maneiras de usar um modulo:
1 - Importando todo o modulo.
2 - Importando apenas uma funcao especifica do modulo (forma recomendada).
"""

from random import random, randint

for numero in range(3):
    print(random())

print(randint(1, 10))