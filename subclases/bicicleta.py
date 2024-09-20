class Bicicleta:
    def __init__(self, marca, modelo, color, tipo):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.tipo = tipo

    def arrancar(self):
        print(f"La bicicleta {self.marca} {self.modelo} está lista para rodar.")

    def frenar(self):
        print(f"La bicicleta {self.marca} {self.modelo} está frenando.")

    def __str__(self):
        return f"Bicicleta(marca={self.marca}, modelo={self.modelo}, color={self.color}, tipo={self.tipo})"