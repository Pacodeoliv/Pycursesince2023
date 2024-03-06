"""
leia do usuario um valor em reais e se o valor for igual a 1250
imprima na tela :voce pode comprar o celular. se nao , se for maior
ou igual a 800 reais : voce precisa economizar um pouco.se nao
imprima : voce nao tem dinheiro suficiente

"""

#Sempre que mexer com dinheiro , usar FLOAT pois pode ter centavos

valor1 = int(input('Pedro tem :'))
valor2 = 1250
valor3 = 800
#if valor1 == 1250
if valor1 >= valor2:
    print('voce pode comprar o celular')
#elif valor1 >= 800
elif valor1 >= valor3:
    print('Voce precisa economizar um pouco mais')
else:
    print('Voce tem o valor suficiente')