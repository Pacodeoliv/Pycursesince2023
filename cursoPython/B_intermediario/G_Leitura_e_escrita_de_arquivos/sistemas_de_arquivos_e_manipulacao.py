"""
Sistema de arquivos - Manipulação

É a continuação da parte de Navegação.
"""

import os

# Descobrindo se um arquivo ou diretório existe
print(os.path.exists('teste.txt'))
print(os.path.exists('pasta1'))

# Diretórios com path relativo
print(os.path.exists('pasta1\\pasta2'))

# Diretórios com path absoluto
print(os.path.exists(('C:\\Users\\Paco de Oliveira\\PycharmProjects\\cursoPython\\B_Intermediario\\'
                      'G_Leitura_e_escrita_de_arquivos\\pasta1\\pasta2')))

# Criando arquivos (melhor forma)
# os.mknod('arquivo-teste.txt')
# OBS.: criando um arquivo via mknod() se o arquivo já existir teremos o erro FileExistsError.

# Criando diretórios (podem ser colocados paths relativos ou absolutos)
os.mkdir('pasta-teste')

# Criando vários diretórios juntos
os.makedirs('pasta3\\pasta4')

# Renomeando
os.rename('pasta1\\pasta2', 'pasta2_renomeada')
# OBS.: se o diretório não existir teremos um FileNotFoundError.
# OBS. 2: se o diretório que queremos renomear não estiver vazio teremos OSError.

# Removendo arquivos
os.remove('arquivo-teste.txt')
# OBS.: cuidado com deleções no código, porque visto que foi deletado não tem como recuperar.

# Removendo diretórios vazios
os.rmdir('pasta1\\pasta2')

# Removendo vários diretórios vazios
os.removedirs('pasta3\\pasta4')