class Pessoa:
    def __init__(self):
        self.nome = "Sou uma pessoa"
        self.habilidades = ["Habilidade 1", "Habilidade 2", "Habilidade 3"]

    def __repr__(self):
        return "Classe Pessoa com propriedades nome e habilidades"

    def __len__(self):
        return len(self.habilidades)


pessoa = Pessoa()
print(pessoa.nome)
print(repr(pessoa))
print(len(pessoa))
