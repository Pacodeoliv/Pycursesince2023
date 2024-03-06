"""
2. Leia do usuário duas quantidades de filmes assistidos e verifique: se a primeira quantidade for maior que 5
 ou a segunda quantidade for, imprima: "Pelo menos uma dessas pessoas assistiu muitos filmes."
"""

film1 = float(input('Carlos ja assistiu :'))
film2 = float(input('Joana ja assistiu: '))

if film1 > 5 or film2 > 5:
    print('Pelo menos uma dessas pessoas assistiu muitos filmes')
else:
    print(f'Carlos viu um total de : {film1} filmes ')
    print(f'Joana viu um total de : {film2} filmes')

