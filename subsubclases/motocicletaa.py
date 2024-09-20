from subclases.bicicleta import Bicicleta

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.cilindrada = cilindrada
        self.velocidad = velocidad

def arrancar (self):
    print(f"La motocicleta {self.marca} {self.modelo} está lista para rodar.")
def frenar (self):
    print(f"La motocicleta {self.marca} {self.modelo} está frenando.")
def __str__(self):
    return f"Motocicleta(marca={self.marca}, modelo={self.modelo}, color={self.color}, tipo={self.tipo}, cilindrada={self.cilindrada}, velocidad={self.velocidad})"
