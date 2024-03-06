"""
MRO - Method Resolution Order

É a ordem de execução dos métodos

Em Python, existem 3 formas para saber o MRO:
- Com a propriedade da classe __mro__ (pelo console)
- Com o método mro()
- Com o help()
"""

# pass = não da erro no codigo mas c onsigo arrumar depois . usado temporariamente

class Pessoa:
    pass


class Desenvolvedor:
    pass


class Funcionario(Pessoa, Desenvolvedor):
    pass


print(Funcionario.mro())
print(help(Funcionario))
