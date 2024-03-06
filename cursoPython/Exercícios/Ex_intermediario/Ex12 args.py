"""
Crie uma funcao para imprimir uma mensagem de uma propaganda personalizada que tenha como parametros o nome do cliente,
o produto dele favorito e informacoes extras. No retorno traga uma mensagem personalizada e no final use a funcao
colocando valores recebidos do usuario.

OBS: receber as informacoes extras , e com o for . antes de usar o for , perguntar a pessoa quantas informacoes ela
vai passar

"""


def propaganda_pers(client, produto_fav, *args_infextra):
    return f'{client} acabou de comprar o seu {produto_fav}, por apenas mais 100 reais ele foi capaz de escolher entre'\
            f' levar mais dois produtos {args_infextra}. Venha participar tambem!'


print(propaganda_pers('Gabriel', 'Caixa de som JBL', 'Fone de ouvido Bluetooth', 'Carregador portatil'))
