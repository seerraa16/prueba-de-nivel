from superclases.vehiculo import Vehiculo



class Coche(Vehiculo):
	def __init__(self, color, ruedas, velocidad, cilindrada):
		super().__init__(color, ruedas)
		self.velocidad = velocidad
		self.cilindrada = cilindrada

	def __str__(self):
		return f"{super().__str__()}, Velocidad: {self.velocidad}, Cilindrada: {self.cilindrada}"