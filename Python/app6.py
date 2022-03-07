# funções python
def dar_boas_vindas():
    print("Bem vindo!")


def dar_boas_vindas_personalizada(nome):
    print(f"Bem vindo (a) {nome}")


def apresentar_lugar(horario, lugar="Nossa Loja"):
    print(f"Conheça {lugar} na horario de funcionamento {horario}")


dar_boas_vindas_personalizada("Geovanni")
apresentar_lugar("08 a 18", "Disney")
