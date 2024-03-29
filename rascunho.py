"""

def leitor_de_horas(segundos):
    unidades = [
        ("ano", 31557600),
        ("mês", 2678400),
        ("dia", 86400),
        ("hora", 3600),
        ("minuto", 60),
        ("segundo", 1),
    ]

    tempo_convertido = []

    for unidade, valor in unidades:
        numero = segundos // valor
        if numero > 0:
            plural = "s" if numero > 1 else ""
            tempo_convertido.append(f"{numero} {unidade}{plural}")
        segundos %= valor

    if len(tempo_convertido) == 1:
        return tempo_convertido[0]
    elif len(tempo_convertido) > 1:
        return ", ".join(tempo_convertido[:-1]) + " e " + tempo_convertido[-1]
    else:
        return "menos de um segundo"


segundos = int(input("Digite a quantidade de segundos: "))
leitura_tempo = leitor_de_horas(segundos)
print(f"Tempo: {leitura_tempo}")
"""

nome = input("qual seu nome?")
idade = input("qual sua idade?")
peso = input("qual seu peso?")
altura = input("qual sua altura?")

print(f" Meu nome é {nome}, tenho {idade} de idade,"
      f"atualmente peso {peso} kilos, minha altura é {altura}")


