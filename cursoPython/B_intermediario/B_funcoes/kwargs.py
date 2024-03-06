"""
Kwargs

Tem a mesma ideia do *args, mas nesse caso usamos com
parametros nomeados e ele e colocado em um dicionario.

OBS: O **kwargs SEMPRE deve estar com dois ** asteriscos.
"""


def enviar_proposta(empresa, investimento, **kwargs):
    return f'A empresa {empresa} tem uma proposta com o '\
            f'investimento {investimento} e a sua proposta e'\
            f'{kwargs}'


print(enviar_proposta('Sunshine', 30_000, proposta='Melhorar a empresa',
                      funcionarios='Contratar mais funcionarios'))
