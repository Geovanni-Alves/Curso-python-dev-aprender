from csv import DictReader, DictWriter

with open("pessoas3.csv", "w", newline="", encoding="utf-8") as arquivo:
    cabecalho = ["nome", "idade", "altura"]
    csv_writer = DictWriter(arquivo, fieldnames=cabecalho)
    csv_writer.writeheader()
    csv_writer.writerow({
        "nome": "Mark",
        "idade": 25,
        "altura": 170
    })
    csv_writer.writerow({
        "nome": "Carol",
        "idade": 19,
        "altura": 160
    })
    csv_writer.writerow({
        "nome": "Robert",
        "idade": 65,
        "altura": 175
    })
with open("pessoas3.csv", "r", newline="", encoding="utf-8") as arquivo_original:
    dados_originais = DictReader(arquivo_original)
    pessoas = list(dados_originais)
    with open("pessoas_v5.csv", "w", newline="", encoding="utf-8") as novo_arquivo:
        cabecalho = ["nome", "idade", "altura"]
        csv_writer = DictWriter(novo_arquivo, fieldnames=cabecalho)
        csv_writer.writeheader()
        for pessoa in pessoas:
            csv_writer.writerow({
                "nome": pessoa["nome"],
                "idade": pessoa["idade"],
                "altura": pessoa["altura"] + " cm"
            })
