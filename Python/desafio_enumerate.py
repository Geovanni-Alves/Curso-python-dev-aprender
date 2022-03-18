frutas = ["Maça", "Laranja", "Morango", "Limão"]
for indice, fruta in enumerate(frutas, 0):
    if indice == 3:
        print(indice, fruta, "Em promoção")
    else:
        print(indice, fruta)
