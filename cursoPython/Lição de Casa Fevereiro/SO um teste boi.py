print('\t ---- sequencia de fibonacci ----')
n = int(input("quantos termos da sequencia de fibonacci voce quer?"))

#comecando com 0 e 1

num1, num2 = 0, 1
contador = 0
while contador < n:
    num3 = num1 + num2
    #Atualizando valores
    num1 = num2
    num2 = num3
    contador += 1
    print(num1)