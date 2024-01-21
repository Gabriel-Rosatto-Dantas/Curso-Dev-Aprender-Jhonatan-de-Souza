# Herança

class Camera:
    def __init__(self, marca, megapixels):
        self.marca = marca
        self.megapixels = megapixels

    def tirar_foto(self):
        print(f'Foto tirada com a camera {self.marca} com a qualidade {self.megapixels} megapixels.')



class CameraCelular(Camera):
    def __init__(self, marca, megapixels, quantidade_de_cameras):
        super().__init__(marca, megapixels)
        self.quantidade_de_cameras = quantidade_de_cameras

    def aplicar_filtro(self, filtro):
        print(f'Aplicando filtro {filtro}.')

    def tirar_foto(self, camera_a_utilizar):
        print(f'Foto tirada com a camera {self.marca} com a qualidade de {self.megapixels} megapixels, utilizando a camera #{camera_a_utilizar}.')

camera_celular = CameraCelular('Sony', '25mp', 4)
camera_celular.aplicar_filtro('Azul')
camera_celular.tirar_foto(2)
