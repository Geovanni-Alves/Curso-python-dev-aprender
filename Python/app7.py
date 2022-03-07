def exibir_cotacao_do_dia(moeda):
    if moeda == "usd":
        print(5.36)


def obter_cotacao_do_dia(moeda):
    if moeda == "usd":
        return 5.36


exibir_cotacao_do_dia("usd")

cotacao = obter_cotacao_do_dia("usd")
if cotacao > 5:
    print("Investir em ações americanas")
else:
    print("Cotação não favorável")
