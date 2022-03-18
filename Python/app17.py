# Enumerate
for indice, numero in enumerate(range(1, 11), 1):
    print(indice, numero)
    if indice == 5:
        print("Estamos na metade da lista")

nomes = ["Geovanni", "Thiago", "Junior", "Dudu"]
#n = 1
for indice, nome in enumerate(nomes, 1):
    print(indice, nome)
    #n += 1
