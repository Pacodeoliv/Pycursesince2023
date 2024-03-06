"""
While

E um laco de repeticao como um For, apensar usado de uma
maneira diferente.
"""

cont = 0 # contador
while cont < 5:
    print(f'Essa frase esta imprimindo pela {cont}ª vez')
    cont += 1



# Se a casquinha for menor ou igual a 5: rode algo, se nao: rode a outra coisa
#'while true' sempre e usado com 'break'

casquinha = 5

while True:
    if casquinha <= 5:
        print(f'A casquinha vale R&{casquinha} .')
        break
    elif casquinha <= 15:
        print(f'Essa casquinha e mais cara, pois vale: R$ {casquinha} . ')
        break
    else:
        print('valor inaceitavel para uma casquinha')
        break
#while true e usado quando precisamos fazer muitas verificoes
