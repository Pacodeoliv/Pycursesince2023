"""
Debuggando codigo

E usado para verificar cada parte do codigo para ver se esta
funcionando corretamente.

Comandos basicos:
l -> lista onde estamos no codigo
n -> vai para a proxima linha
p -> imprime uma variavel
c -> continua a execucao ou termina
"""

nome_aluno = 'Julio'
idade = 25
breakpoint()
info_aluno = f'{nome_aluno} tem a idade {idade}'
print(info_aluno)
