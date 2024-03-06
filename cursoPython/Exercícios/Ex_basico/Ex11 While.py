"""Recebe do usuário o valor de uma caixa de lápis da FaberCastell,
depois faça um while que repita 5 vezes, cada vez que repetir você adiciona 2 reais de imposto
 no valor falado. No final imprima o valor total da caixa de lápis."""

vlr1 = float(input('Essa caixa de lapis vale: '))

cont = 0 # contador
while cont <= vlr1:
    vlr1 += 2
    print(f'Essa frase esta imprimindo pela {vlr1}ª vez')



