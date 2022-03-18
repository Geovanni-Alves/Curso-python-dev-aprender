# Herança
from ast import Pass


class Camera:
    def __init__(self, marca, megapixels):
        self.marca = marca
        self.megpixesls = megapixels

    def tirar_foto(self):
        print(
            f"Foto tirada com a camera {self.marca} com a qualidade {self.megpixesls} megapixels"
        )


class CameraCelular(Camera):
    def __init__(self, marca, megapixels, quant_cameras):
        super().__init__(marca, megapixels)
        self.quant_cameras = quant_cameras

    def aplicar_filtro(self, filtro):
        print(f"aplicando filtro {filtro}")

    def tirar_foto(self, camera_a_utilizar):
        print(
            f"Foto tirada com a camera {self.marca} com a qualidade {self.megpixesls} megapixels"
            f"utilizando a camera {camera_a_utilizar}"
        )


camera_celular = CameraCelular("Sony", "48mp", 5)
camera_celular.aplicar_filtro("Azul")
camera_celular.tirar_foto(2)
