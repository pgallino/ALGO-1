"""Dada una partida en forma de una lista de tuplas de la forma <personaje>,<movimiento> y un número k, 

imprimir por pantalla todos los movimientos notables de cada personaje y cuántas veces se usaron. 

Se dice que un movimiento es notable si el personaje lo utilizó más de k veces durante la partida. 

Ejemplo:

movimientos = [("Pikachu", "Impactrueno"), ("Charizard", "Lanzallamas"), ("Pikachu", "Ataque Rápido"), ("Charizard", "Lanzallamas")]

>>> imprimir_notables(movimientos, 1)
Charizard - Lanzallamas (2)"""

def imprimir_notables(movimientos, k):

    diccionario = {}
    
    for tupla in movimientos:
        clave = tupla[0] + " - " + tupla[1]
        diccionario[clave] = diccionario.get(clave, 0) + 1
    
    for clave in diccionario:
        if diccionario[clave] > k:
            print(f"{clave} ({diccionario[clave]})")