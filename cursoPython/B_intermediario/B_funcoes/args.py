"""
Args - arguments

E um parametro usado para receber valores quando voce nao sabe o limite, ou seja,
e como se voce fosse receber varios valores  sem saber qual e o ultimo.

OBS: O args e transformado em uma tupla, entao lembre-se que tuplas sao imutaveis

OBS: O *args e sempre escrito com * asterisco, ate podemos mudar o nome dele
caso necessario, como: *informacoes.

OBS: O *args SEMPRE deve vir no final dos parametros, afinal se ele nao tem
limite, como o Python vai saber quando terminar o *args se voce colocar antes?
entao ele tem que vir por ultimo .

EX: def enviar_email(*args, email, nome):
# Se o args for no comeco como no EX a cima , ele nunca vai ter fim para dar inicio ao "email"

"""


def enviar_email(nome, email, *args):
    # Se necessario posso por uma doc_string aqui pra explicar oque e o args
    return f'O email foi enviado a(o) {nome} com email {email} e com as '\
            f'informacoes extras: {args}'


print(enviar_email('Julio', 'julia_silva@gmail.com', 'Programador', '23 anos'))
# O email foi enviado a(o) Julio com email julia_silva@gmail.com e com as informacoes extras: ('Programador', '23 anos')
# O *args vem entre parenteses por ser uma tupla!
