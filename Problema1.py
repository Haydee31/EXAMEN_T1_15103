import random
class Equipo:
     def __init__(self, nombre, partidosGanados = 0, partidosPerdidos = 0, setGanados = 0):
        self.nombre = nombre
        self.partidosGanados = partidosGanados
        self.partidosPerdidos = partidosPerdidos
        self.setGanados = setGanados
equipo1 = Equipo("Leones")
equipo2 = Equipo("Águilas")

def RegistraSet(equipo_ganador):
    if equipo_ganador == 1:
        equipo1.setGanados += 1
        if equipo1.setGanados == 3:
            equipo1.partidosGanados += 1
            equipo2.partidosPerdidos += 1
            equipo1.setGanados = 0
            equipo2.setGanados = 0
    else:
        equipo2.setGanados += 1
        if equipo2.setGanados == 3:
            equipo2.partidosGanados += 1
            equipo1.partidosPerdidos += 1
            equipo1.setGanados = 0
            equipo2.setGanados = 0 
def Puntos():
    return random.randint(10, 28)
def PuntosExtras():
    return random.randint(0, 6)
def JugarPartido():
    puntos1 = Puntos()
    puntos2 = Puntos()
    print(f"{equipo1.nombre}: {puntos1} pts")
    print(f"{equipo2.nombre}: {puntos2} pts")
    while not (puntos1 >= 25 or puntos2 >= 25):
        puntos1 += PuntosExtras()
        puntos2 += PuntosExtras()
        print(f"==> Puntos extras - {equipo1.nombre}: {puntos1} pts | {equipo2.nombre}: {puntos2} pts")
    if puntos1 > puntos2:
        RegistraSet(1)
        print(f"=> Ganó el set: {equipo1.nombre}")
    else:
        RegistraSet(2)
        print(f"-> Ganó el set: {equipo2.nombre}")