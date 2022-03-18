""" print('''Estamos codando todos os dias
e estou aprendendo muito!!
sera que vai mais linhas,
isso eu nao sabia, que legal ''')

print('Ola meu nome é \nGeovanni')
print('Codas todos \'os dias\'')
print('Arquivo encontrato em \\c:drive\\arquivo.txt')           
nome = "Geovanni"
print(nome)
print(len(nome))

print("codar!")
print("vamos 'codar!'")
print("vamos \n'codar'") """
""" nome = "Geovanni"
email = "geo-estevam@hotmail.com"
print(f"Ola {nome}, voce cadastrou o email {email}, essa informacao esta correta") """
""" nome = "Carol"
hobby = "Ouvir Musica"
print(f"Ola sou a {nome} e gosto de {hobby}")

b = "ba"
parte2 = "nica"
a = "a"
r = "ri"
parte1 = "eletrô"
t = "te"

print(f"{b}{t}{r}{a} {parte1}{parte2}") """
""" nome_curso = "edicao de video"
print(nome_curso.upper())
print(nome_curso.lower())
print(nome_curso.strip())
print(nome_curso.lstrip())
print(nome_curso.rstrip())
print(nome_curso.find("cao"))
print(nome_curso.replace("video", "musica"))
print("https:relogio".replace("relogio", "carro")) """
""" a = "é"
b = "MELHOR"
c = "QUE"
d = "feito"
e = "perfeito"

print(f"{a.upper()} {b.lower()} {d.upper()} {c.lower()} {e.upper()}")
 """
""" teclado = "Teclado"
print(teclado[2])
print(teclado[4])
print(teclado[-1])
print(teclado.index("l"))
print(teclado[teclado.index("l")])

frase = "Clean Code"
print(frase.rindex("C"))  """
""" biblioteca = "Biblioteca"
print(biblioteca.index("o"))

frase1 = "Desenvolvimento De Aplicações"
print(frase1[frase1.rindex("D"):frase1.rindex("s") +1]) """
""" frase = "Ola, bem-vindo a este treinamento!"
print(frase.split())
print(frase.split(","))
print(frase.split("-"))
nomes = "Geovanni, Lorena,Goku"
print(nomes.split())
print(nomes.split(","))
hashtags = "music #guitar #gamer #coder #python"
print(hashtags.split())
print(hashtags.split("#"))
print(hashtags.split("#", 3))
hashtags_separadas_por_espaco = hashtags.split(" ")
print(hashtags_separadas_por_espaco)
print(",".join(hashtags_separadas_por_espaco))
print(".".join(hashtags_separadas_por_espaco))
print(" ".join(hashtags_separadas_por_espaco)) """

""" frase1 = "Desafio manipulacao de strings"
frase2 = "jhonatan,rafael,carol,camilla"
frase1_separada = frase1.split()
frase2_separada = frase2.split(",")
print(",".join(frase1_separada))
print(" & ".join(frase2_separada)) """

"""
import math
a = 20
b = 20.5
print(type(a))
print(type(b))
a += 1
print(a)

print(round(5.7))
print(math.ceil(2.2)) """


""" print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)

# Criar uma data
data_exemplo = datetime(2022, 3, 3)
print(data_exemplo)

data_lancamento = datetime.strptime(
    input("quando e da data de lancamento: "), "%d/%m/%Y")

print(data_lancamento)
print(type(data_lancamento))

data_atual = datetime.now()
prazo = data_lancamento - data_atual

print(prazo.days) """ """ """

""" from datetime import datetime
aniversario = datetime(2022, 3, 26)
dias_para_aniversario = aniversario - datetime.now()

print(dias_para_aniversario)
 """
