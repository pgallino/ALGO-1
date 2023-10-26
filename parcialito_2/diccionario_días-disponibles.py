"""Escribir una función que dado un diccionario cuyas claves son los nombres de los integrantes de un grupo de amigos,

 y los valores asociados una lista de los días de la semana que están disponibles, devuelva una lista de los días que pueden juntarse.

Por ejemplo, si recibe: {'Juan':['MIE', 'VIE', 'SAB'], 'Jose':['VIE', 'SAB', 'DOM'], 'Jorge':['JUE', 'VIE', 'SAB']} debe devolver ['VIE', 'SAB']."""

def enlista_dias_disponibles1(diccionario):
    dias_apariciones = {}
    lista_personas = diccionario.keys()
    lista_resultado = []

    for clave in diccionario:
        for día in range(len(diccionario[clave])):
            dias_apariciones[diccionario[clave][día]] = dias_apariciones.get(diccionario[clave][día], 0) + 1

    for clave in dias_apariciones:
        if dias_apariciones[clave] == len(lista_personas):
            lista_resultado.append(clave)

    return lista_resultado
    
def enlista_dias_disponibles2(diccionario):                                                 #versiones 2 y 3 no cuentan porque tienen &
    listas_dias = diccionario.values()
    lista_conjuntos = []

    for lista in listas_dias:
        lista_conjuntos.append(set(lista))

    for indice in range(1, len(lista_conjuntos)-1):
        lista_conjuntos[indice] = lista_conjuntos[indice - 1] & lista_conjuntos[indice]
        conjunto = lista_conjuntos[indice]
        
    return list(conjunto)



def enlista_dias_disponibles3(diccionario):
    listas_dias = list(diccionario.values())
    conjunto_dias = set(listas_dias[0])
    for clave in diccionario:
        conjunto_dias = set(diccionario[clave]) & conjunto_dias
    return list(conjunto_dias)
