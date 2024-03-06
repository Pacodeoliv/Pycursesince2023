"""
1. Leia do usuário dois tempos de músicas e verifique: se o primeiro tempo for maior que 120 minutos
ou o segundo for,imprima: "Uma dessas pessoas está viciada em música."
"""

msc1 = int(input('A musica que pedro ouve tem :'))
msc2 = int(input('A musica de maria tem: '))

if msc1 > 120:
    print('Uma dessas pessoas esta viciada em musica')
elif msc2 > 120:
    print('Uma dessas pessoas esta viciada em musica')
else:
    print(f'A musica de pedro tem {msc1} minutos e de maria {msc2} minutos')
