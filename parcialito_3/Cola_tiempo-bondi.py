
"""En la parada del colectivo 130 pueden ocurrir dos eventos diferentes:

Llega una persona
Llega un colectivo con n asientos libres, y se suben al mismo todas las personas que están esperando, en orden de llegada, hasta que no quedan asientos libres.

Cada evento se representa con una tupla que incluye:

El instante de tiempo (cantidad de segundos desde el inicio del día)
El tipo de evento, que puede ser 'p' (persona) o 'c' (colectivo).
En el caso de un evento de tipo 'c' hay un tercer elemento que es la cantidad de asientos libres.
Escribir una función que recibe una lista de eventos, ordenados cronológicamente, y devuelva el promedio de tiempo de espera de los pasajeros en la parada."""

from Cola import Cola

def promedio_espera(eventos):
    '''
    calcula el promedio de tpo de espera de los pasajeros en la parada del bondi
    '''
    cola = Cola()
    personas = 0
    tiempo_total = 0

    for tupla in eventos:
        if tupla[1] == "p":
            cola.encolar(tupla[0])
            personas += 1
        elif tupla[1] == "c":
            for _ in range(tupla[2]):
                if cola.frente == None:
                    break
                tiempo = cola.desencolar()
                tiempo_total += (tupla[0] - tiempo)
    
    return tiempo_total / personas

eventos = [(35,'p'), (43,'p'), (80,'c',1), (98,'p'), (142,'c',2)]
print(promedio_espera(eventos))