"""
Crie um named_tuple de material tenha como parametros o tipo dele ,o valor e a marca e apartir dessa tupla faca
uma copia e apartir da copia faca um slicing dos dois primeiros parametros (valores)
"""

from collections import namedtuple

# Namedtuple
celular = namedtuple('celular' , 'tipo valor marca')

# Parametros
iphoneXr = celular(tipo='Smartphone', valor='1500 Reais', marca='Apple')

# Fazendo a copia
copia = iphoneXr

# Slicing
print(copia[:2])
