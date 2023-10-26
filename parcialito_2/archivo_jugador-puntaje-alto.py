"""Se tiene un archivo de texto donde cada línea es de la forma nombre_jugador,puntaje_1,puntaje_2,...,puntaje_n, 

representando una serie de puntajes obtenidos por un jugador (puede haber cualquier cantidad de puntajes para cada jugador, pero todos tienen al menos uno). 

Los puntajes no tienen decimales. 

Escribir un función que reciba el nombre de un archivo con la forma descripta y el nombre de un archivo destino,

y escriba en él líneas de la forma nombre_jugador,puntaje_mas_alto, siendo puntaje_mas_alto el más alto de entre los puntajes de ese jugador.

Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos deben quedar cerrados."""

def cargar_puntaje_mas_alto(ruta_archivo_origen, ruta_archivo_destino):

    with open(ruta_archivo_origen) as archivo, open(ruta_archivo_destino, "w") as destino:
        
        for linea in archivo:

            linea = linea.rstrip("\n").split(",")
            jugador = linea.pop(0)
            lista_puntajes = list(map(int, linea))
            puntaje_mas_alto = max(lista_puntajes)
            destino.write(f"{jugador},{puntaje_mas_alto}\n")