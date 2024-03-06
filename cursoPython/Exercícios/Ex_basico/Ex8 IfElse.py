"""
Leia do usuario um ID de um desenvolvedor , se o ID for igual a '1' imprima desenvolvedor junior
se nao, se o ID for igual a 2 , imprima desenvolvedor pleno
se nao , se o ID for igual a 3 , imprima desenvolvedor senior
senao , imprima ID invalido
"""

vid1 = int(input('O ID dele e: '))
if vid1 == 1:
    print('Voce e um Dev. Junior')
elif vid1 == 2:
    print('Voce e um Dev. Pleno ')
elif vid1 == 3:
    print('voce e um Dev. senior')
else:
    print('ID invalido')