from subclases.coche import Coche
from subclases.bicicleta import Bicicleta
from subsubclases.camioneta import Camioneta
from subsubclases.motocicletaa import Motocicleta

if __name__ == "__main__":
    mi_vehiculo = Coche("Naranja fosforito", 4, 180, 2000)
    print(mi_vehiculo)
    deportiva = "deportiva"  # Define the variable deportiva
    mi_vehiculo2 = Bicicleta("purpura", 2, deportiva)
    print (mi_vehiculo2)
    mi_vehiculo3 = Camioneta("BMW", "x5", 1000)
    print (mi_vehiculo3)
    mi_vehiculo4 = Motocicleta("Yamaha", "FZ", "Negra", "Deportiva",2, 250, 1500)