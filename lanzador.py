from subclases.coche import Coche
from subclases.bicicleta import Bicicleta
from subsubclases.camioneta import Camioneta
from subsubclases.motocicletaa import Motocicleta

def lanzador_main():
    vehiculos = []

    coche1= Coche("Naranja mandarina", 4, 140, 2000)
    vehiculos.append(coche1)
    print(coche1)

    Bici1 = Bicicleta("Gris", 2, "Urbana")
    vehiculos.append(Bici1)
    print(Bici1)

    camioneta1 = Camioneta("Rosa", 4, 2849, 160, 2500)
    vehiculos.append(camioneta1)
    print(camioneta1)

    Bici2 = Bicicleta("Verde Brocoli", 2, "Deportiva")
    vehiculos.append(Bici2)
    print(Bici2)

    Camioneta2 = Camioneta( "Negro", 4, 1500, 140, 3000)
    vehiculos.append(Camioneta2)
    print(Camioneta2)



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