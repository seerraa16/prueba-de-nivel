from subclases.coche import Coche


class Camioneta(Coche):
    def __init__(self, color, ruedas, capacidad_carga, velocidad, cilindrada):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.capacidad_carga = capacidad_carga

        def __str__(self):
            return f"Camioneta(color={self.color}, ruedas={self.ruedas}, capacidad_carga={self.capacidad_carga}, velocidad={self.velocidad}, cilindrada={self.cilindrada})"
        
        def cargar(self):
            print("La camioneta está cargada")
        
        def descargar(self):
            print("La camioneta está descargada")
        
        def arrancar(self):
            print("Arrancando la camioneta")
        
        def frenar(self):
            print("Frenando la camioneta")
    
    def cargar(self):
        print("La camioneta está cargada")
    
    def descargar(self):
        print("La camioneta está descargada")
    
    def arrancar(self):
        print("Arrancando la camioneta")
    
    def frenar(self):
        print("Frenando la camioneta")
    

