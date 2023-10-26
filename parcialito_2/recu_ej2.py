# Se cuenta con un archivo CSV con pasajes de avión con el siguiente formato:
# `id_pasajero;origen;destino`
# Escribir una función que recibe la ruta a un archivo con este formato y devuelva un diccionario 
# donde las claves son los id_pasajero y como valor una lista con los lugares donde estuvo 
# el pasajero (SIN REPETIR).

# Escribir el codigo debajo de esta linea
def lugares_visitados(ruta):
    
    with open(ruta) as archivo:

        diccionario = {}

        for linea in archivo:

            linea = linea.rstrip("\n").split(";")

            pasajero, origen, destino = linea

            diccionario[pasajero] = diccionario.get(pasajero, [])

            if not origen in diccionario[pasajero]:
                diccionario[pasajero].append(origen)
            
            if not destino in diccionario[pasajero]:
                diccionario[pasajero].append(destino)
        
        return diccionario


# Pruebas
resultado = lugares_visitados('pasajes.csv')
assert sorted(['buenos aires', 'madrid', 'san pablo', 'bogota']) == sorted(resultado['1029'])
assert sorted(['san pablo', 'bogota']) == sorted(resultado['18840'])
assert sorted(['buenos aires', 'san pablo', 'madrid']) == sorted(resultado['8456'])
assert sorted(['mendoza', 'buenos aires'] ) == sorted(resultado['29384'])