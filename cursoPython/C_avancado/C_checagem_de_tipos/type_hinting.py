"""
Type Hinting

É a maneira de mostrar estaticamente o tipo de um dado.

Annotations = o tipo em sí
É quando anota um tipo do Type Hinting.
"""


def add_juros(preco: float) -> float:
    return preco + 20.5


print(add_juros(10))
