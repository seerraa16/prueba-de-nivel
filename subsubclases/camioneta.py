from subclases.coche import Coche


class Camioneta(Coche):
    def __init__(self, color, ruedas, capacidad_carga, velocidad, cilindrada):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.capacidad_carga = capacidad_carga


    def __str__(self):
        return f"Camioneta, {super().__str__()}, Capacidad de carga: {self.capacidad_carga}"
    

