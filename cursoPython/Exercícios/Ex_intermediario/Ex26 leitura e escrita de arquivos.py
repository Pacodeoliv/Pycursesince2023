"""
Crie um arquivo chamado "restaurante.txt" que tenha dentro dele refeições de um restaurante.
 Depois crie um arquivo Python chamado "atualização". Dentro desse novo arquivo:
1º Abra o arquivo com o modo de abertura "r+";
2º Escreva no arquivo três pratos;
3º Volte para o começo do arquivo;
4º Leia tudo.
"""


with open('restaurante.txt', 'r+') as arquivo:
    arquivo.write('marmitex\n')
    arquivo.write('comida de vo\n')
    arquivo.write('acostela')
    arquivo.seek(3)
    arquivo.read()
    print(arquivo.read())
