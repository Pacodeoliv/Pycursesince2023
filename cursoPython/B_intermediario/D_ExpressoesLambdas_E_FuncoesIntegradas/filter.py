"""
Filter

Como diz o proprio nome , e usado para filtrar dados de uma colecao.
"""

# Biblioteca(Biblio e basicamente um programa externo) para dados estatisticos
import statistics

# Valores do bingo
bingo = [10, 41, 54]

# caluclando a media com mean()
media = statistics.mean(bingo)

print(f'Media: {media}')

# O filter() recebe dois parametros , uma funcao e um iteravel
maiores_que_media = filter(lambda valor: valor > media, bingo)
# OBS : Os valores usados no filter serao excluidos depois de serem usados, sao valores temporarios

print(list(maiores_que_media))