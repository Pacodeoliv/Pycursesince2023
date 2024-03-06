"""
Crie um datetime com a data "09/08/2008", adicione 6 dias (usando o combine)
e imprima o weekday. Depois pegue esse date e transforme em str usando strftime e imprima o resultado.
"""

import datetime

data = datetime.datetime(2008, 8,9)
print(data)

data_soma = datetime.datetime.combine((data +
                                 datetime.timedelta (days = 6)), datetime.time())

print(data_soma)

datasoma = data_soma.strftime('%d/%m/%Y')

print(datasoma)
