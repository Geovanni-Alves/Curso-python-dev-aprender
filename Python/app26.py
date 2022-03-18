import os

# with open("celulares.txt", "w") as arquivo:
#     arquivo.write("Celular1")

# nomes = ["Geovanni", "Lorena"]
# numeros = [1, 2, 3, 4, 5, 6]
# with open("numeros.txt", "a", newline="") as arquivo:
#     for numero in numeros:
#         arquivo.write(str(numero) + os.linesep)

with open("nomes.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha)
