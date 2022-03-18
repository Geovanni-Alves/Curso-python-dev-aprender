from operator import itemgetter
produtos = [
    {"nome": "celular", "preço": 1500},
    {"nome": "monitor", "preço": 500},
    {"nome": "microfone", "preço": 300}
]
produtos.sort(key=itemgetter("preço"))
print(produtos)

equipamento_filmagem = [
    ("tripe", 300),
    ("camera", 1700),
    ("iluminacao", 200),
]
equipamento_filmagem.sort(key=itemgetter(1), reverse=True)
print(equipamento_filmagem)

cotacao_moedas = [["usd", 5.25], ["brl", 1.56], ["eur", 6.47]]
cotacao_moedas.sort(key=itemgetter(1))
print(cotacao_moedas)
