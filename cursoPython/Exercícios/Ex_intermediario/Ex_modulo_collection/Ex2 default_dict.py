"""

Crie um default dict que tenha um valor padrao de pecas de computador tenha como valor default de sua preferencia ,
depois adicione tres elementos , crie uma copia e apartir da copia remova o 2 elemento. no final itere usando a copia

"""

from collections import defaultdict

pc = defaultdict(lambda: 'Pecas nao encontradas')

print(pc[1])

pc[2] = 'gtx 980'
pc[3] = 'gt 710'
pc[4] = 'i5 3330'
print(pc[2],pc[3],pc[4])


copia = pc.copy()

print(copia)
copia.pop(2)
print(copia)

for numero, peca in copia.items():
    print(f' pecas: {numero}')



