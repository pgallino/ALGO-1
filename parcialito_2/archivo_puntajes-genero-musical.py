"""Se cuenta con un archivo llamado ratings.csv que contiene en cada línea los puntajes que los usuarios de un conocido sitio de música dan a los artistas que escuchan.

El formato del archivo es usuario,genero,artista,puntaje. 
 
Se pide realizar una función que reciba por parámetro un nombre de género musical 
 
y cree un nuevo archivo .csv que contenga todos los puntajes correspondientes a los artistas del género. 

El formato debe ser usuario,artista,puntaje, y el nombre del archivo creado debe ser el nombre del género. 

(ejemplo, si el género recibido es "rock", el archivo se debe llamar rock.csv).

Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos deben quedar cerrados."""

import csv

def puntajes_por_genero(ruta_archivo, genero_elegido):
    
    ruta_archivo_destino = f"{genero_elegido}.csv"

    with open(ruta_archivo) as archivo, open(ruta_archivo_destino, "w") as destino:

        lector = csv.DictReader(archivo)
        escritor = csv.writer(destino)

        for fila in lector:
            usuario = fila["usuario"]
            genero = fila["genero"]
            artista = fila["artista"]
            puntaje = fila["puntaje"]

            if genero == genero_elegido:
                escritor.writerow([usuario, artista, puntaje])

def puntajes_por_genero2(ruta_archivo, genero_elegido):

    ruta_archivo_destino = f"{genero_elegido}_version2.csv"

    with open(ruta_archivo) as archivo, open(ruta_archivo_destino, "w") as destino:

        next(archivo)

        for linea in archivo:
            usuario, genero, artista, puntaje = linea.rstrip("\n").split(",")

            if genero == genero_elegido:
                destino.write(f"{usuario};{artista};{puntaje}\n")


