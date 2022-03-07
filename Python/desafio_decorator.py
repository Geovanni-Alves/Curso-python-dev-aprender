from datetime import datetime
hora = datetime


def teste_decorator(funcao):
    def controle():
        print(hora.now())
        funcao()
        print(hora.now())
    return controle


@teste_decorator
def retornar_hora():
    print("Monitoranto hora")


retornar_hora()
