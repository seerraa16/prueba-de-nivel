from subclases.bicicleta import Bicicleta

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, velocidad, cilindrada, tipo):
        super().__init__(ruedas, color, tipo)
        self.cilindrada = cilindrada
        self.velocidad = velocidad

    def __str__(self):
        return f"Motocicleta, {super().__str__()}, Velocidad: {self.velocidad}, Cilindrada: {self.cilindrada}"