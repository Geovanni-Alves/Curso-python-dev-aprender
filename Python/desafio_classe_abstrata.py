from abc import ABC, abstractclassmethod


class Monitor(ABC):
    @abstractclassmethod
    def aumentar_claridade(self, valor):
        pass

    @abstractclassmethod
    def reduzir_claridade(self, valor):
        pass


class MonitorFullHD(Monitor):
    def aumentar_claridade(self, valor):
        print(f"aumentando claridade em {valor} pontos!")

    def reduzir_claridade(sefl, valor):
        print(f"reduzindo claridade em {valor} pontos !")


monitor = MonitorFullHD()
monitor.aumentar_claridade(int
                           (input("Digite o valor para aumentar a claridade: ")))
monitor.reduzir_claridade(int
                          (input("Digite o valor para reduzir a claridade: ")))
