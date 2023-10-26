"""Se tiene un archivo con el siguiente formato <nombre persona>;<lugar>;<momento en que la persona estuvo alli>.

Escribir una funcion que reciba la ruta a este archivo y el nombre de una persona y devuelva un conjunto con todas las personas con las que tuvo contacto.
Una persona tuvo contacto con otra si estuvieron en el mismo lugar en el mismo momento).

Notas:

El archivo no se encuentra ordenado bajo ningún criterio y no posee errores de formato ni de tipo de datos. No posee encabezado.

El archivo puede recorrerse una única vez.

Cada persona puede haber estado en multiples lugares en múltiples momentos distintos (inclusive múltiples momentos para el mismo lugar).

El tipo de dato para el "momento" no importa, tratarlo como una cadena."""

def contador_encuentros(ruta_archivo, nombre_persona):
    
    with open(ruta_archivo) as archivo:

        diccionario={}

        conjunto = set()
        
        for linea in archivo:
            
            linea = linea.rstrip("\n").split(";")

            diccionario[linea[0]] = diccionario.get(linea[0], []) + [(linea[1],linea[2])]    #diccionario con cada persona como clave, con lista de tuplas de (lugar,momento) como valor

        for clave in diccionario:

            for tupla in diccionario[clave]:                                                 #chequea si las tuplas de los demás estan en la lista del nombre_parametro

                if clave != nombre_persona and tupla in diccionario[nombre_persona]:

                    conjunto.add(clave)                                                      #agrega los nombres de los que tuvieron contacto

        return conjunto
            


