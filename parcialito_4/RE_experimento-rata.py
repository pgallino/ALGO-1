"""Escribir una función recursiva que simule el siguiente experimento:

Se tiene una rata en una jaula con 3 caminos, entre los cuales elige al azar (cada uno tiene la misma probabilidad),

si elige el 1 luego de 3 minutos vuelve a la jaula, si elige el 2 luego de 5 minutos vuelve a la jaula,

en el caso de elegir el 3 luego de 7 minutos sale de la jaula. La rata no aprende, siempre elige entre los 3 caminos con la misma probabilidad,

pero quiere su libertad, por lo que recorrerá los caminos hasta salir de la jaula.

La función debe devolver el tiempo que tarda la rata en salir de la jaula."""

import random

lista_caminos = []
def simular_experimento():
    n = random.randint(1,3)
    if n == 3:
        lista_caminos.append(3)
        return 7
    
    elif n == 2:
        lista_caminos.append(2)
        return simular_experimento() + 5

    else:
        lista_caminos.append(1)
        return simular_experimento() + 3

print(simular_experimento())
print(lista_caminos)