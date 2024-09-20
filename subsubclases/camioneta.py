from subclases.coche import Coche


class Camioneta(Coche):
	def __init__(self, color, ruedas, velocidad, cilindrada, capacidad_carga):
		super().__init__(color, ruedas, velocidad, cilindrada)
		self.capacidad_carga = capacidad_carga

def __str__(self):
	return "color {}, {} km/h, {} ruedas, {} cc, {} kg de carga".format(self.color, self.velocidad, self.ruedas, self.cilindrada, self.capacidad_carga)
camioneta = Camioneta("blanco", 100, 180, 1300, 1500)
def descargar(self):
    print("La camioneta está descargando")
print(camioneta)
camioneta.descargar()
