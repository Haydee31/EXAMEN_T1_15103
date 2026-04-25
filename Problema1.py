import random
class Equipo:
     def __init__(self, nombre, partidosGanados = 0, partidosPerdidos = 0, setGanados = 0):
        self.nombre = nombre
        self.partidosGanados = partidosGanados
        self.partidosPerdidos = partidosPerdidos
        self.setGanados = setGanados
equipo1 = Equipo("Leones")
equipo2 = Equipo("Águilas")
