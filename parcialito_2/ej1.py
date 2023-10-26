# 1. Se pide escribir una función que calcule el ganador de una liga de fútbol a
# partir de los resultados de los partidos realizados. La función recibe una
# lista de tuplas de 4 elementos con el siguiente formato:
#  (nombre_equipo1, goles_equipo1, nombre_equipo2, goles_equipo2)

# Ejemplo: `("Barcelona", 1, "Real Madrid", 2)`.

# La función devuelve el nombre del equipo ganador. En caso de haber más de
# un equipo con puntuación máxima, devolver uno cualquiera de entre ellos.

# Reglas de puntaje de la liga: el equipo ganador de un partido recibe 2
# puntos, y el perdedor 0 puntos. En caso de empate, cada uno de los dos
# equipos recibe 1 punto.

# Completar la siguiente funcion
def calcular_ganador_liga(partidos):

    diccionario = {}
    puntaje = 0

    for i in range(len(partidos)):

        if partidos[i][1] > partidos[i][3]:
            diccionario[partidos[i][0]] = diccionario.get(partidos[i][0], 0) + 2

        elif partidos[i][1] < partidos[i][3]:
            diccionario[partidos[i][2]] = diccionario.get(partidos[2][i], 0) + 2

        else:
            diccionario[partidos[i][2]] = diccionario.get(partidos[i][2], 0) + 1
            diccionario[partidos[i][0]] = diccionario.get(partidos[i][0], 0) + 1
    
    for clave in diccionario:
        if diccionario[clave] > puntaje:
            puntaje = diccionario[clave]
            campeon = clave
    
    return campeon


partidos = [
    ("Real Madrid", 2, "Barcelona", 1),
    ("Real Madrid", 1, "Valencia", 1),
    ("Valencia", 1, "Barcelona", 2)
]
assert calcular_ganador_liga(partidos) == "Real Madrid"