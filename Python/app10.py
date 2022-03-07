# Decorators
def meu_docorator(funcao):
    def wrapper():
        print("Antes")
        funcao()
        print("Depois")
    return wrapper


@meu_docorator
def parabenizar():
    print("Parabens!!!")


# resultado = meu_docorator(parabenizar)
# resultado()
parabenizar()
