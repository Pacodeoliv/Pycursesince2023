"""
. Leia do usuário duas alturas e verifique: se a primeira altura for maior que 1.80 e a segunda altura também,
 imprima: "Essas pessoas são altas."
"""
alt1 = float(input('A altura de Pedro e: '))
alt2 = float(input('A altura de Maria e: '))

if alt1 > 1.80 and alt2 <= 1.80:
    print(f'A altura de pedro e: {alt1},ele e alto')
    print(f'A altura de Maria e: {alt2}')
elif alt2 > 1.80 and alt1 <= 1.80:
    print(f'A altura de pedro e: {alt1}')
    print(f'A altura de Maria e: {alt2}, ela e alta')
elif alt1 > 1.80 and alt2 > 1.80:
    print('essas pessoas sao altas')
else:
    print('altura invalida')

"""
nao to conseguindo fazer 
"""
