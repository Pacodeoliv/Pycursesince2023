"""
Crie uma função chamada "fazer_login" que tenha como parâmetro "função". Dentro dela imprima uma mensagem de
login feito com sucesso e depois retorne essa função.

Depois de tudo isso, crie outra função (decorada) chamada "dados" que tenha como parâmetros "email" e "senha",
 e retorne uma mensagem contendo esses dados.

No final use a segunda função passando os dados.
"""


def fazer_login(funcao):
    print("Login feito com sucesso!")
    return funcao


@fazer_login
def dados(email, senha):
    return f"Dados recebidos: Email: {email}, Senha: {senha}"


print(dados('paco@gmail.com', 1456235))
