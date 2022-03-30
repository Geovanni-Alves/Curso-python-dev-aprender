from pprint import pprint


def eh_par(numero):
    valor = numero % 2
    if valor == 0:
        return True
    else:
        return False


print([i for i in range(1, 11) if eh_par(i)])


cores = ["vermelho", "azul", "verde", "amarelo", "rosa", "preto"]

pprint([str(cores.index(cor) + 1) + " - " + cor for cor in cores])

participantes = ["joel", "jessica", "maria",
                 "cris", "larissa", "rafael", "marcus", "john"]
pagamento_realizado = ["joel", "jessica", "maria", "cris"]

print([participante + " PAGO" if participante in pagamento_realizado
       else participante + " DEVENDO" for participante in participantes])
