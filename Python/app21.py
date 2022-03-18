try:
    internet = None
    print("Fazendo conexão com a " + internet)
except TypeError as erro_tp:
    print("Não há conexão com a internet")
finally:
    print("Compra não processada")

try:
    valor = int(input("Digite um valor: "))
    print(valor / 0)
except ZeroDivisionError as erro_div0:
    print("Não e possivel dividir por zero!")
except ValueError as erro_value:
    print("Favor digitar apenas números")
finally:
    print("A operação foi cancelada")
