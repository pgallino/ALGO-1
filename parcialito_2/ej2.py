# 2. Implementar una función que dado el nombre de un archivo CSV de la forma
# `película;año;actor1,actor2,...,actorN`
# y el nombre de un arctor, devuelva un diccionario donde cada año tenga asociado 
# una lista con todas las películas en los que el actor participó.

# Cualquier línea con datos inválidos (cualquier campo vacío o el año no es un número)
# debe ser ignorada y la ejecución debe continuar. Se puede suponer que todas las líneas contienen
# **siempre** tres elementos separados por `;`.

# Ejemplo:

# ```
# peliculas.csv
# -------------
# Memento;2000;Guy Pearce,Joe Pantoliano
# Iron Man 3;2013;Robert Downey Jr,Guy Pearce
# Sexto Sentido;;Bruce Willis
# Pulp Fiction;1994;John Travolta,Samuel L. Jackson
# Rules Of Engagement;2000;Guy Pearce
# ```

# >>> peliculas_años('peliculas.csv', 'Guy Pearce')
# { 2000: ['Memento', 'Rules Of Engagement'],
#   2013: ['Iron Man 3'] }

# Completar la siguiente funcion
def peliculas_años(archivo, actor):

    diccionario = {}
    
    with open(archivo) as f:

        for linea in f:
            linea = linea.rstrip("\n").split(";")
            if linea[1] == "" or linea[1].isdigit() == False:
                continue
            
            if actor in linea[2]:
                diccionario[int(linea[1])] = diccionario.get(int(linea[1]),[]) + [linea[0]]
    
    return diccionario




res = {
    2000: ['Memento', 'Rules Of Engagement'],
    2013: ['Iron Man 3']
}
assert peliculas_años('peliculas.csv', 'Guy Pearce') == res