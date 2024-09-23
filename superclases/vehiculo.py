

class Vehiculo():
	def __init__(self, color, ruedas):
		self.color = color
		self.ruedas = ruedas

	def __str__(self):
		return f" vehiculo, Color: {self.color}, Ruedas: {self.ruedas}"
