import os
frutas = ["Banana", "Maça", "Abacaxi", "Melancia", "Laranja"]
cores = ["Vermeho", "Amarelo", "Azul", "Verde", "Cinza"]
linguagens = ["Python", "Java", "Clipper", "Visual Basic", "C++"]

with open("frutas.txt", "w", newline="") as arquivo:
    for fruta in frutas:
        arquivo.write(fruta + os.linesep)

with open("frutas.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha)

with open("frutas.txt", "a", newline="") as arquivo:
    for cor in cores:
        arquivo.write(cor + os.linesep)

with open("top_5_linguages.txt", "w", newline="") as arquivo:
    for linguagem in linguagens:
        arquivo.write(linguagem + os.linesep)

for cor in cores:
    with open(f"{cor}.txt","w"):
        ...