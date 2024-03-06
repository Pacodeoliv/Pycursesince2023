"""
Crie um Ordered Dict que tenha como chave uma bebida e tenha como valor (receba do usuario tem que ter dois ,
um pro valor e outro com a idade) o ano que ela foi criada , depois adicione tres elementos recebidos do
usuario a partir do dicionario crie um deepcopy (dar preferencia pro deepcopy smepre) e a partir
da copia remova um elemento
"""



"""
from collections import OrderedDict
bebidas = OrderedDict()
for b in range(3):
    b1 = str(input('digite uma bebida :'))
    v1 = int(input('digite uma idade :'))
    bebidas[b1] = v1

print(bebidas)
#deepcopy 
copia = bebidas.copy()

# ele esta certo , porem nao e possivel remover um item com pop de algo criado com "for"
"""

from collections import OrderedDict
bebidas = OrderedDict()
#receba do usuario
b1 = str(input('digite uma bebida :'))
v1 = int(input('digite uma idade :'))
b2 = str(input('digite uma bebida :'))
v2 = int(input('digite uma idade :'))
b3 = str(input('digite uma bebida :'))
v3 = int(input('digite uma idade :'))

#Adicionando ao dicionario
bebidas[b1] = v1
bebidas[b2] = v2
bebidas[b3] = v3

print(bebidas)
#pra seprar um do outro pra ler
print('-=' * 10)

#copia e o resto
copia = bebidas.copy()
copia.pop(b1)
print(copia)
