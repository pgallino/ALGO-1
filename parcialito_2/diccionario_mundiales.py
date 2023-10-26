"""a. Escribir una función que dada una lista de tuplas, con el el año en el que se disputó un mundial de fútbol y el equipo campeón de ese año, 

devuelva un diccionario con la cantidad de mundiales ganados por cada equipo. 

Un ejemplo de la lista de tuplas: [(1930, 'Uruguay'), (1934, 'Italia'), (1938, 'Italia'), ...] 


b. Escribir otra función que reciba el diccionario generado en el punto anterior y devuelva una lista con el/los paises que ganaron más mundiales."""

def contador_mundiales_por_pais(lista): #punto a

    cantidad_de_mundiales_por_pais = {}

    for i in range(len(lista)):
        cantidad_de_mundiales_por_pais[lista[i][1]] = cantidad_de_mundiales_por_pais.get(lista[i][1], 0) + 1

    return cantidad_de_mundiales_por_pais

def encontrar_pais_mas_ganador(cantidad_de_mundiales_por_pais): #punto b

    paises_mas_ganadores = []
    cant_max_mundiales = max(cantidad_de_mundiales_por_pais.values())

    for clave in cantidad_de_mundiales_por_pais:
        if cantidad_de_mundiales_por_pais[clave] == cant_max_mundiales:
            paises_mas_ganadores.append(clave)

    return paises_mas_ganadores

