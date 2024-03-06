"""
sistema de arquivos e navegacao

Para usar manipulacao de arquivos do sistema operacional precisamos importar e usar o modulo OS.

OS - Operating System

Path absoluta x Path relativo:
Absoluto -> E a path (caminho) inteiro ate um arquivo/diretorio.
Relativo -> e uma parte desse path ate um arquivo/diretorio.
"""

import os

print(os.getcwd())  # Pega o pah absoluto do diretorio que estamos usando

print('-=' * 20)

os.chdir('..') # Volta 1 diretorio
print(os.getcwd())

print('-=' * 20)

print(os.path.isabs('C:\\Users\\Paco de Oliveira'))  # Verifica se o path e absoluto ou relativo
# OBS.: para computadores Windows os paths sao escritos com contra barra \, mas no codigo precisamos colocar
# duas contra barras

print('-=' * 20)

import sys
print(sys.platform)  # Verificando o sistema operacional

print('-=' * 20)

juntando = os.path.join(os.getcwd(), 'pasta1')  # Junta um path com o outro, nesse caso um diretorio com outro.
os.chdir(juntando)

# Lista os diretorios de pasta do seu path
print(os.listdir('C:\\Users\\Paco de Oliveira\\Desktop\\PycharmProjects\\cursoPython\\B_intermediario\\'
                 'G_Leitura_e_escrita_de_arquivos'))

print('-=' * 20)

scan = os.scandir('C:\\Users\\Paco de Oliveira\\Desktop\\PycharmProjects\\cursoPython\\B_intermediario')

arquivos = list(scan)

print(arquivos)
print(arquivos[0].is_dir())
print(arquivos[0].is_file())
print(arquivos[0].name())
print(arquivos[0].path())
print(arquivos[0].stat())

# OBS.: precisa do close() !
scan.close()
