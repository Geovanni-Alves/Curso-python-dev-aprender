def gerar_nome_completo(nome, sobrenome):
    print(f"Ola {nome} {sobrenome}, seja bem vindo ao Python")


def calcular_valores(preco, quantidade=1):
    print(f"Preço do produto: {preco}, voce esta levando {quantidade},"
          f" portanto o total é: {preco * quantidade}")


gerar_nome_completo("Geovanni", "Estevam")
calcular_valores(50, 5)
