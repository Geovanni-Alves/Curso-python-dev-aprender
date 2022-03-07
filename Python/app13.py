valores = [1, 2, 2, 2, 2, 23, 4, 5, 6, 7, 8, 10]
anos = [2020, 2030, 2040, 2050, 2060, 2070, 2080, 2090]
# adicionar ao final da lista
valores.append(11)
print(valores)
# unir listas
valores.extend(anos)
print(valores)
# adicionar lista
nova_lista = valores + anos
print(nova_lista)
# inserir um novo valor na lista
anos.insert(2, 2031)
print(anos)
# extrair item com base no indice
anos_2020 = anos.pop(0)
print(anos_2020)
# remover o item da lista
anos.remove(2050)
del anos[1:6]
print(anos)
# contando a ocorrencia de um valor na lista
print(valores.count(2))
# resetar os itens dentro de uma lista (excluir todos items)
valores.clear()
print(valores)
