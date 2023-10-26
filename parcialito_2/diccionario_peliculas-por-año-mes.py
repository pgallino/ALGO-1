"""Se cuenta con un diccionario cuyas claves son títulos de películas, y su valor asociado su fecha de estreno, una cadena en formato DD/MM/AAAA. 
Escribir una función que dado un diccionario de estas características, 
devuelva otro diccionario cuyas claves sean el mes y el año en formato MM/AAAA, y su valor una lista con todas las películas que se estrenaron en dicho mes y año."""

def agrupar_peliculas_por_año_mes(diccionario):
    peliculas_por_año = {}

    for clave in diccionario:
        clave_nueva = diccionario[clave].split("/")
        clave_nueva = f"{clave_nueva[1]}/{clave_nueva[2]}"
        peliculas_por_año[clave_nueva] = peliculas_por_año.get(clave_nueva, []) + [clave]
        
    return peliculas_por_año

