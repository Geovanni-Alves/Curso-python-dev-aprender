def somar(*valores, b):
    print(valores)
    for valor in valores:
        b += valor
    print(b)


somar(10, 50, 20, 5, 5, b=50)
# *args

# kwargs (Keyword arguments)


def concatenar(**palavras):
    frase = ""
    for palavra in palavras.values():
        frase += palavra + " "
    print(frase)


concatenar(a="nos", b="somos", c="pythonistas", d="profissionais")
