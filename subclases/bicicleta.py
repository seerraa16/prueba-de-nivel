from superclases.vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)

        self.tipo = tipo

    def arrancar(self):
        print(f"La bicicleta {self.color} está lista para rodar.")

    def frenar(self):
        print(f"La bicicleta {self.color} está frenando.")

    def __str__(self):
        return f"Bicicleta(color={self.color}, tipo={self.tipo}, ruedas={self.ruedas})"