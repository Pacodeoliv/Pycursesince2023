"""
Declare um dicionario que tenha como chave o nome de uma musica e tenha como valor o tempo da musica , depois disso
remova o quarto elemento , faca um Shallow Copy e a partir da copia adicione um elemento. Em seguida verifique
se o elemento esta presente e por ultimo limpe o dicionario
"""

musicas = {'Zoom': 2.44, 'Confident': 1.58, 'Text me': 2.53, 'Hold on': 3.34}
del musicas['Hold on']
copia = musicas
copia['Slow'] = 2
print('Slow' in copia)
copia.clear()
print(copia)