"""Se pide implementar la clase TwitterUser con los siguientes métodos:

__init__(): recibe como parámetro el nombre del usuario.

tweet(): recibe como parámetro un mensaje (se debe validar que no sobrepase los 280 caracteres) y lo agrega —con la fecha actual— a la lista de tuits del usuario. 

(Para obtener la fecha actual, se puede importar el módulo datetime, e invocar datetime.datetime.now())

follow(): recibe como parámetro otro usuario (de tipo TwitterUser) y lo guarda como un usuario al que se está siguiendo.

get_timeline(): devuelve una lista con los mensajes que tuitearon los usuarios a los que se está siguiendo.

Debe ser una lista de tuplas tal que: (fecha, nombre_usuario, mensaje). Este método no toma parámetros, y la lista devuelta debe estar ordenada por fecha."""

import datetime

class TwitterUser:

    def __init__(self, nombre):

        self.nombre = nombre
        self.tuits = []
        self.siguiendo = []

    def tweet(self, mensaje):
        if len(mensaje) < 280:
            
            fecha = datetime.datetime.now()

            self.tuits.append([fecha, self.nombre, mensaje])
        
        else:
            raise Exception("Se sobrepasaron los 280 caracteres")
    
    def follow(self, otro):
        self.siguiendo.append(otro)

    def get_timeline(self):
        timeline = []
        for i in range(len(self.siguiendo)):
            for j in range(len(self.siguiendo[i].tuits)):
                timeline.append(self.siguiendo[i].tuits[j])
        
        timeline = list(sorted(timeline))
        for i in range(len(timeline)):
            timeline[i][0] = str(timeline[i][0])
            timeline[i] = tuple(timeline[i])
        return timeline

