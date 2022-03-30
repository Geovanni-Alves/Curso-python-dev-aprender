# list compreheension
# [expressão for membro in iterável]
from pprint import pprint
pprint([[i for i in range(1, 6)] for x in range(5)])

nomes = ["Geovanni", "Rafael", "Marcus", "Eduardo"]


def aprovar_pessoa(nome):
    return(nome + " APROVADO")


def eh_numero_par(numero):
    valor = numero % 2
    if valor == 0:
        return True
    else:
        return False


# lista compreheension com condicionais
print([aprovar_pessoa(nome) for nome in nomes if nome != "Rafael"])

pprint([i for i in range(20) if eh_numero_par(i)])
