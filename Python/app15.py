from itertools import zip_longest
# Trabalhando com multiplas listas
a_lista = ["A", "B", "C", "D", "E"]
b_lista = [1, 2, 3, 4, 6]
for a, b in zip(a_lista, b_lista):
    print(a)
    print(b)

produtos = ["produto 1", "produto 2", "produto 3", "produto 4", "produto 5"]
precos = [250, 150, 220, 550, 50]
for a, b in zip(produtos, precos):
    print(f"Salvando produto {a} valor R$ {b}")

titulos = ["titulo 1", "titulo 2", "titulo 3", "titulo 4"]
descricoes = ["descricao 1", "descricao 2", "descricao 3"]
for titulo, descricao in zip_longest(titulos, descricoes):
    print(f"Encontramos o {titulo} com a descrição: {descricao}")
