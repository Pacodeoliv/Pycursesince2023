"""
Checagem de tipos com MyPy

Para instalar:
pip install mypy

Para executar: mypy nome_do_modulo.py

OBS.: O Mypy só funciona se vc estiver usando o Type Hinting
"""


def add_juros(preco: float) -> float:
    return preco + 20.5


print(add_juros(10))