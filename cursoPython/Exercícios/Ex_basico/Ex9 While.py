"""
Leia do usuário o valor de uma caneca, e faça um while true que rode: se o valor for menor ou igual a 20, imprima:
"A caneca está em promoção", senão se o valor for menor ou igual a 40, imprima: "A caneca nao está sem promoção",
senão imprima: "A caneca está mais alta do que o normal"
"""

caneca = float(input('A caneca vale: '))
while True:
    if caneca <= 20:
        print('A caneca está em promoção')
        break
    if caneca <= 40:
        print('A caneca está sem promoção')
        break
    else:
        print('A caneca está mais alta do que o normal')
        break

