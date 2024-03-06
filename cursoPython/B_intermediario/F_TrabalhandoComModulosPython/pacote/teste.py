def imprimir():
    print('Usando teste')

if __name__ == '__main__':
    print('Executando o modulo teste diretamente.')
else:
    print(f'O modulo teste foi importado, seu nome: {__name__}')
