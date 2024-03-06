""""
List Comprehension

Usamos para criar novas listas a partir de outra iteravel (colecao).

Sintaxe/estrutura do List Comprehension:
[ dado for dado in iteravel]

para entender melhor como o List Comprehension funciona, devemos dividi-lo em duas
partes:

- Primeira parte: for DADO in ITERAVEL
- Segunda parte: DADO
(Basicamente nos dividimos o que vem depois de for na primeira parte, e na segunda
colocamos o que vem antes do for para poder ler e entender melhor.)
"""

sorvetes = [ 4.99, 3.45, 9.10, 4.1]

sorvetes_com_desconto = [preco / 2 for preco in sorvetes]
# Primeira parte: for preco in sorvetes = para cada preco em sorvetes
# Segunda parte: preco / 2 = preco pela metade
print(sorvetes_com_desconto)

# Podemos tambem colocar Estruturas Condicionais (if)

sorvetes_mais_caros = [preco for preco in sorvetes if preco > 5]
# Primeira parte: for preco in sorvetes if preco > 5 = para cada preco em sorvetes
# Se o sorvete for maior que 5
# Segunda parte: preco = pega o sorvete 
print(sorvetes_mais_caros)
