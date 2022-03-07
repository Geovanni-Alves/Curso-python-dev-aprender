from datetime import datetime


def depositar_dinheiro():
    print("depositanto dinheiro")

    def depositando_dolar():
        print("depositando dolares ")

    def depositando_reais():
        print("depositando reais")

    depositando_dolar()
    depositando_reais()


depositar_dinheiro()


def pai(numero):
    def filho_1():
        print("Sou filho 1")

    def filho_2():
        print("Sou filho 2")
    if numero == 1:
        return filho_1


resultado = pai(1)
resultado()
