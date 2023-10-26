"""Escribir una función que reciba una ruta a un archivo de pokemones con el siguiente formato <pokemon>;<tipo>;<pos_x>,<pos_y>,

 y un diccionario de gimnasios (cada clave es el nombre de un gimnasio, y el valor asociado, su posicion, dada como una tupla (pos_x, pos_y))

 y escriba en un archivo de salida el pokemon, su tipo y su gimnasio más cercano. 
 
 El archivo de salida debe tener el siguiente formato: <pokemon;<tipo>;<gimnasio más cercano>.

Para calcular la distancia entre pokemon y gimnasio se utiliza distancia manhattan:

dist(p1, p2) = |p1_x - p2_x| + |p1_y - p2_y|

Notas:

El archivo no se encuentra ordenado bajo ningún criterio y no posee errores de formato ni de tipo de datos. No posee encabezado.
El archivo puede recorrerse una única vez y no entra entero en memoria."""

def cargar_gimnasio_mas_cercano(ruta_archivo_pokemon, destino, diccionario_gym):
    with open(ruta_archivo_pokemon) as archivo_origen, open(destino, "w") as archivo_destino:

        for linea in archivo_origen:
            pokemon, tipo, pos_x, pos_y = linea.rstrip("\n").split(";")
            lista_puntos = list(diccionario_gym.values())
            distancia_anterior = 9999999999999

            for clave in diccionario_gym:
                distancia_gym = (abs((int(pos_x) - diccionario_gym[clave][0])) + abs((int(pos_y) - diccionario_gym[clave][1])))

                if distancia_gym <= distancia_anterior:
                    distancia_anterior = distancia_gym
                    gym_cercano = clave

            archivo_destino.write(f"{pokemon};{tipo};{gym_cercano}\n")


