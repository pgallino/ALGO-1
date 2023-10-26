"""Implementar una función que recibe el nombre de un archivo, cuyo contenido esta en formato csv, con el ganador del torneo de water polo de cada año,

y genere un nuevo archivo con la cantidad de veces que ganó cada equipo. El archivo que se recibe tiene los datos de la forma año,equipoCampeon, de a uno por línea.

Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos deben quedar cerrados."""

def contar_campeonatos_equipo(ruta_archivo, ruta_destino):

    with open(ruta_archivo) as origen, open(ruta_destino, "w") as destino:
        diccionario = {}
        for linea in origen:
            linea = linea.rstrip("\n").split(",")
            diccionario[linea[1]] = diccionario.get(linea[1], 0) + 1

        for clave in diccionario:
            destino.write(f"{clave},{diccionario[clave]}\n")
