"""
Manipulando data e hora

O Python tem um módulo built-in (integrado) para se trabalhar com data
e hora chamado datetime.
"""

import datetime

data = datetime.datetime(2022, 7, 12, 3, 19, 56)
print(data)

data_agora = datetime.datetime.now()
print(data_agora)

print('-=' * 20)

"""
Trabalhando com deltas de data e hora

delta = data_final - data_inicial
"""

data_agora = datetime.datetime.now()

cinco_dias = datetime.timedelta(days=5)

diferenca = cinco_dias + data_agora
print(diferenca)

print('-=' * 20)

"""
Métodos de data e hora
"""

# Mudanças ocorrendo à meia-noite - combine()
data = datetime.datetime.combine((datetime.datetime.now() +
                                  datetime.timedelta(days=1)), datetime.time())
print(data)

# OBS.: dias da semana - segunda = 0, terça = 1, quarta = 2, etc (usando weekday()
# dá para ver qual é o dia).

print(data.weekday())

print('-=' * 20)

"""
Formatando datas/horas com strftime() (String Format Time)

dd/mm/yyyy hora:minuto
"""

hoje = datetime.datetime.today()
hoje_formatado = hoje.strftime('%d/%m/%y')

print(hoje)
print(hoje_formatado)

nascimento = datetime.datetime.strptime('06/02/1997', '%d/%m/%Y')
print(nascimento)