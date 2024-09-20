from subclases.coche import Coche


class Camioneta(Coche):
	def __init__(self, marca, modelo, capacidad_carga):
		super().__init__(marca, modelo)
		self.capacidad_carga = capacidad_carga
