from turtle import Turtle, forward
# inicializar uma turtle
# t = Turtle()
# t.speed(1)  # velocidade
# t.forward(100)  # movimentar para frente

# t.right(90)  # rotacionar para direita
# t.forward(100)

# t.left(90)  # rotacionar para esquerda
# t.forward(100)

# t.backward(200)  # movimentar para tras

# input()  # para congelar e nao fechar a janela

t = Turtle()
t.speed(1)
continuar = "s"
pixels = 0
rotacionar_pixels_esquerda = 0
rotacionar_pixels_direita = 0
while continuar == "s":
    direcao = input("Para qual direção devemos ir "
                    "(f = frente, t = trás)? ")
    if direcao == "f":
        pixels = int(input("Quantos pixels devemos movimentar"
                           " para frente? "))
    else:
        pixels = int(input("Quantos pixels devemos movimentar"
                           " para trás? "))
    rotacionar = input(
        "Rotacionar para (d = direita, e = esquerda, n = não rotacionar)? ")
    if rotacionar != "n":
        if rotacionar == "d":
            rotacionar_pixels_direita = int(
                input("Quanto para a direita devemos rotacionar: "))
        elif rotacionar == "e":
            rotacionar_pixels_esquerda = int(
                input("Quanto para a esquerda devemos rotacionar: "))
    if direcao == "f" and rotacionar == "n":
        t.forward(pixels)
    elif direcao == "f" and rotacionar == "d":
        t.right(rotacionar_pixels_direita)
        t.forward(pixels)
    elif direcao == "f" and rotacionar == "e":
        t.left(rotacionar_pixels_esquerda)
        t.forward(pixels)
    if direcao == "t" and rotacionar == "n":
        t.backward(pixels)
    elif direcao == "t" and rotacionar == "d":
        t.right(rotacionar_pixels_direita)
        t.backward(pixels)
    elif direcao == "t" and rotacionar == "e":
        t.left(rotacionar_pixels_esquerda)
        t.backward(pixels)

    continuar = input("Continuar andando (s = sim)? ")
