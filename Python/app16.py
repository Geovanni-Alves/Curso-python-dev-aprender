# Tuplas
from array import array
import re
sites = ("youtube.com", "facebook.com", "instagram.com")
valores = (23, 43, 65)
# uniao de tuplas
dados_do_Sistema = sites + valores
print(dados_do_Sistema[2])

# Arrays
# interios, numeros decimais e characteres
numeros = array("i", [1, 2, 3, 4, 5, 6])
numeros.append(10)
numeros.insert(5, 200)
numeros.pop(1)
numeros.remove(5)
del numeros[0]
print(numeros)

# range (geradores)
for numero in range(10, 30, 2):
    print(numero)
resultado = list(range(0, 201, 10))
print(resultado)
