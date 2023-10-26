"""Escribir la clase Partido, que recibe en el constructor dos cadenas que corresponden al nombre del equipo local y el visitante (en ese orden).
además, tiene los siguientes metodos:

cargar_resultado: recibe dos números enteros, que corresponden a los goles convertidos por el local y el visitante (en ese orden).
obtener_ganador: devuelve el nombre del ganador, o none si hubo empate.
obtener_perdedor: similar a obtener_ganador

Escribir la clase Liga, que tiene los siguientes metodos:

cargar_partido: recibe un objeto de clase Partido, y guarda los datos necesarios.
obtener_campeon: devuelve una cadena con el nombre del equipo que más puntos tiene.
si hay varios con el mismo puntaje maximo, devolver el nombre de cualquiera.

se otorgan 3 puntos por partido ganado, 1 por partido empatado y 0 por partido perdido."""

class Partido:

    def __init__(self, equipo_local, equipo_visitante):

        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante

    def cargar_resultado(self, goles_local, goles_visitante):
        
        self.goles_local = goles_local
        self.goles_visitante = goles_visitante
    
    def obtener_ganador(self):

        if self.goles_local > self.goles_visitante:
            return self.equipo_local
        elif self.goles_local < self.goles_visitante:
            return self.equipo_visitante
        elif self.goles_local == self.goles_visitante:
            return None

    def obtener_perdedor(self):

        if self.goles_local > self.goles_visitante:
            return self.equipo_visitante
        elif self.goles_local < self.goles_visitante:
            return self.equipo_local
        elif self.goles_local == self.goles_visitante:
            return None

class Liga:

    def __init__(self):

        self.liga = {}

    def cargar_partido(self, partido):

        if partido.obtener_ganador() == None:
            self.liga[partido.equipo_local] = self.liga.get(partido.equipo_local, 0) + 1
            self.liga[partido.equipo_visitante] = self.liga.get(partido.equipo_visitante, 0) + 1
        
        if not partido.obtener_ganador() == None:
            self.liga[partido.obtener_ganador()] = self.liga.get(partido.obtener_ganador(), 0) + 3
            self.liga[partido.obtener_perdedor()] = self.liga.get(partido.obtener_perdedor(), 0) + 0
            
    def obtener_campeon(self):

        puntaje_maximo = 0

        for clave in self.liga:
            if self.liga[clave] > puntaje_maximo:
                puntaje_maximo = self.liga[clave]
                campeon = clave
        return campeon