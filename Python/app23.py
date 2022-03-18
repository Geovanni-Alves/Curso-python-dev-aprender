# classe
class Computador:
    sistema_operacional = "Windows 10"

    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.mermoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def ligar(self):
        print("Estou ligando o computador")

    def desligar(self):
        print("Estou desligando")

    def exibir_dados_do_computador(self):  # metodo comum
        print(f"Computador da marca {self.marca}, com {self.mermoria_ram}, e"
              f"que usa a placa de video {self.placa_de_video}")

    @classmethod
    def computador_escritorio(cls, memoria_ram):
        return cls("Dell", memoria_ram, "Placa de video Barata")

    @classmethod
    def computador_pesado(cls, memoria_ram):
        return cls("Dell", memoria_ram, "Placa de video Top RTX")

    @staticmethod
    def roda_programas_pesados(memoria_ram):
        if memoria_ram >= 8:
            return True
        else:
            return False


# computador_escritorio = Computador.computador_escritorio("8 gb")
# computador_jogos = Computador.computador_pesado("16 Gb")


# computador1 = Computador("Dell", "16gb", "AMD 970")
# print(computador1.marca)
# print(computador1.mermoria_ram)
# print(computador1.placa_de_video)
# computador1.ligar()
# computador1.desligar()
# computador1.exibir_dados_do_computador()
# Computador.sistema_operacional = "Linux"
# print(Computador.sistema_operacional)
# print(computador1.sistema_operacional)

# computador_escritorio.exibir_dados_do_computador()
# computador_jogos.exibir_dados_do_computador()

print(Computador.roda_programas_pesados(16))
