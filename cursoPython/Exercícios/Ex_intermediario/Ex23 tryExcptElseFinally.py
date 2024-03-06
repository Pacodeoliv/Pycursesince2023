"""
Crie um código que:
1º No try: tente receber um sabor preferido de sorvete de uma pessoa.
2º No except: pegue o erro "TypeError" caso ela digite um tipo totalmente diferente.
3º No else: imprima uma mensagem personalizada com o sabor digitado.
4º No finally: imprima uma mensagem de finalização personalizada.
"""

try:
    sabor_preferido = str(input('Digite o seu sabor favorito:'))
except ValueError:
    print('voce nao digitou um sabor, por favor digite um dos sabores aceitos!')
else:
    print(f'O sabor digitado foi {sabor_preferido}')
finally:
    print('Obrigado por participar!')
