from csv import DictReader, DictWriter
import csv

# with open("pessoas.csv") as arquivo:
#     dados = DictReader(arquivo)
#     for dado in dados:
#         print(dado["Id"] + " " + dado["First Name"])

with open("computadores.csv", "w", newline="", encoding="utf-8") as arquivo:
    cabecalho = ["Marca", "Preço", "Ano de Lançamento"]
    csv_writer = DictWriter(arquivo, fieldnames=cabecalho)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Marca": "Asus",
        "Preço": 2500,
        "Ano de Lançamento": 2010
    })
    csv_writer.writerow({
        "Marca": "Dell",
        "Preço": 3500,
        "Ano de Lançamento": 2020
    })
    csv_writer.writerow({
        "Marca": "Acer",
        "Preço": 2900,
        "Ano de Lançamento": 2015
    })

with open("computadores.csv", "r", newline="", encoding="utf-8") as arquivo_original:
    dados_originais = DictReader(arquivo_original)
    computadores = list(dados_originais)
    with open("computadores_v2.csv", "w", newline="", encoding="utf-8") as novo_arquivo:
        cabecalho = ["Marca", "Preço", "Ano de Lançamento"]
        csv_writer = DictWriter(novo_arquivo, fieldnames=cabecalho)
        csv_writer.writeheader()
        for computador in computadores:
            csv_writer.writerow({
                "Marca": computador["Marca"],
                "Preço": "R$" + computador["Preço"],
                "Ano de Lançamento": computador["Ano de Lançamento"]
            })
