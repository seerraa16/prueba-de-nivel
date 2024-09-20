from subclases.coche import Coche


class Camioneta(Coche):
	def __init__(self, color, ruedas, velocidad, cilindrada, capacidad_carga):
		super().__init__(color, ruedas, velocidad, cilindrada)
		self.capacidad_carga = capacidad_carga
