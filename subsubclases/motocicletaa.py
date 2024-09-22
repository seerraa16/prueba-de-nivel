from subclases.bicicleta import Bicicleta

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, velocidad, cilindrada, tipo):
        super().__init__(ruedas, color, tipo)
        self.cilindrada = cilindrada
        self.velocidad = velocidad


    def arrancar(self):
        print("Arrancando la motocicleta")

    def pedalear(self):
        print("Las motocicletas no se pedalean")

    def __str__(self):
        return f"Motocicleta(marca={self.marca}, modelo={self.modelo}, color={self.color}, tipo={self.tipo}, cilindrada={self.cilindrada})"