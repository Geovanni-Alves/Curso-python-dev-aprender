# dicionario

dicionario_pessoa = {"nome": "Geovanni", "idade": 18, "altura": 1.70}
print(dicionario_pessoa)

pessoa_2 = dict(nome="Geo", idade=37, altura=1.70)
print(pessoa_2)

print(pessoa_2["idade"])

# chaves disponiveis
print(dicionario_pessoa.keys())
# valores do dicionario
print(dicionario_pessoa.values())
print(dicionario_pessoa.items())
# iterar sobre um dicionario
for item in dicionario_pessoa.items():
    print(item)
    print(item[1])
