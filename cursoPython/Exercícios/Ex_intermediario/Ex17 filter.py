"""
Crie uma lista de valores de bebidas de um restaurante, depois pegue a média desses valores.
Filtre os valores que são apenas menores que a média e no final imprima esses valores.
"""

import statistics

#valores das bebidas
bebidas = [80, 95, 40, 15, 20]

# Calculando a media com mean()
media = statistics.mean(bebidas)



# O filter() recebendo dois parametros, uma funcao e um iteravel
menores_que_media = filter(lambda valor: valor < media, bebidas)
# OBS : Os valores usados no filter serao excluidos depois de serem usados, sao valores temporarios


# Imprimindo os valores
print(list(menores_que_media))
