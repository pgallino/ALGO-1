"""Ejercicio 155 recursion

Alan, Bárbara y Grace juegan al ping-pong. El que gana un partido sigue jugando, mientras que el que lo pierde es reemplazado por el que no jugaba.

El primer partido es entre alan y barbara. Se gana una cerveza el primero que gana tres partidos seguidos. 

Implementar una función recursiva que simule este juego y devuelva quien ganó. Suponer que la probabilidad de ganar un partido es igual para ambos.

Nota: para simular el resultado de cada parido en forma aleaoria, utilizar la función random.choice."""

from random import randint

def _pingpong(alan, barbara, grace, perdedor):

    if alan == 3:
        return "alan"
    
    elif barbara == 3:
        return "barbara"
    
    elif grace == 3:
        return "grace"
    
    if perdedor == 1:
    
        ganador = randint(2,3)

        if ganador == 2:
            perdedor = 3
        
        else:
            perdedor = 2

    elif perdedor == 2:
        
        ganador = randint(1,3)

        if ganador == 1:
            perdedor = 3
        
        else:
            perdedor = 1
    
    elif perdedor == 3:

        ganador = randint(1,2)

        if ganador == 2:
            perdedor = 1
        
        else:
            perdedor = 2
    
    print(f"el ganador fue {ganador}")

    if ganador == 1:
        return _pingpong(alan + 1, barbara, grace, perdedor)
    
    elif ganador == 2:
        return _pingpong(alan, barbara + 1, grace, perdedor)
    
    elif ganador == 3:
        return _pingpong(alan, barbara, grace + 1, perdedor)

def pingpong():
    ganador = randint(1,2)
    if ganador == 1:
        print("ganó 1")
        return _pingpong(1,0,0,2)
    else:
        print("ganó 2")
        return _pingpong(0,1,0,1)

print(pingpong())