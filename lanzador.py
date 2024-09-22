from subclases.coche import Coche
from subclases.bicicleta import Bicicleta
from subsubclases.camioneta import Camioneta
from subsubclases.motocicletaa import Motocicleta

def lanzador_main():
    vehiculos = []

    mi_vehiculo = Coche("Rojo", 4, 180, 2000)
    vehiculos.append(mi_vehiculo)
    print(mi_vehiculo)

    mi_vehiculo2 = Bicicleta("Azul", 2, "Urbana")
    vehiculos.append(mi_vehiculo2)
    print(mi_vehiculo2)

    mi_vehiculo3 = Camioneta("Rosa", 4, 2849, 160, 2500)
    vehiculos.append(mi_vehiculo3)
    print(mi_vehiculo3)

    mi_vehiculo4 = Bicicleta("Verde Brocoli", 2, "Deportiva")
    vehiculos.append(mi_vehiculo4)
    print(mi_vehiculo4)
    mi_vehiculo5 = Camioneta( "Negro", 4, 1500, 140, 3000)
    vehiculos.append(mi_vehiculo5)
    print(mi_vehiculo5)

    mi_vehiculo6 = Motocicleta( "Blanca", 2, 220, 1200, "Deportiva")
    vehiculos.append(mi_vehiculo6)
    print(mi_vehiculo6)

    mi_vehiculo4 = Motocicleta("Negra",2, 100, 1000, "Urbana")
    vehiculos.append(mi_vehiculo4)
    print(mi_vehiculo4)

    def catalogar(vehiculos, ruedas=None):
        if ruedas is not None:
            vehiculos_filtrados = [v for v in vehiculos if v.ruedas == ruedas]
            print(f"Se han encontrado {len(vehiculos_filtrados)} vehículos con {ruedas} ruedas:")
            for v in vehiculos_filtrados:
                print(v)
        else:
            for v in vehiculos:
                print(v)

    catalogar(vehiculos)
    catalogar(vehiculos, 0)
    catalogar(vehiculos, 2)
    catalogar(vehiculos, 4)