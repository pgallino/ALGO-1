# Escribir una funcion que dada una matriz representada 
# como una lista de listas de numeros (donde cada sublista representa una fila), 
# devuelva una lista con los maximos de cada
# columna. 

# Ejemplo:
# 	maximos_columnas([
#					 [1, 2, 8, 4],
# 					 [6, 7, 3, 3], -> [6, 7, 8, 9]
# 					 [6, 5, 4, 9]])


def maximo_columnas(matriz):
    maximos = []            #creo una lista para los maximos

    if not matriz:           #matriz vacía es igual a false, si no hay matriz, retorna maximos vacio
        return maximos

    for j in range(len(matriz[0])):       #la j representa la cantidad de columnas, entonces j va desde 0 hasta el largo de cualquier fila.
        potenciales_maximos = []                        #armo una lista con los elementos de cada columna
        for i in range(len(matriz)): 
            potenciales_maximos.append(matriz[i][j])             #agrego los elementos de cada columna a la lista
        maximos.append(max(potenciales_maximos))                    #con la funcion max obtengo el maximo de cada columna y lo agrego a la lista de los maximos
    return maximos