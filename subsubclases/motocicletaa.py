from subclases.bicicleta import Bicicleta

class Motocicleta(Bicicleta):
    def __init__(self, color, modelo, cilindrada):
        super().__init__(color, modelo)
        self.cilindrada = cilindrada

    def arrancar(self):
        print("Arrancando la motocicleta")

    def pedalear(self):
        print("Las motocicletas no se pedalean")