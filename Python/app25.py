# Polimorfismo
# print(10 + 20)
# print("Ola" + " Dev!")
# print(len("Livro"))
# print(len([25, 20, 30]))
# print(len({"teste", "teste2"}))
class Carro:
    def ligar(self):
        print("Ligando o carro")


class Moto:
    def ligar(self):
        print("Ligando a moto")


def iniciar(veiculo):  # metodo polimorfico
    veiculo.ligar()


carro = Carro()
moto = Moto()
iniciar(carro)
iniciar(moto)


class Pessoa:
    def apresentar(self, nome, idade=None, profissao=None):  # Função Polimorfica
        if idade and profissao != None:
            print(f"{nome},{idade},{profissao}")
        elif idade != None:
            print(f"{nome},{idade}")
        elif profissao != None:
            print(f"{nome},{profissao}")
        else:
            print(f"{nome}")


pessoa = Pessoa()
pessoa.apresentar("Geovanni")
pessoa.apresentar("Lorena", 35)
pessoa.apresentar("Ada", 30, "Programadora")
