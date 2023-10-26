# Escribir una función `anteponer_pares` que recibe una lista de números y devuelve una nueva lista con los elementos 
# reordenados, de forma tal que todos los números pares aparezcan antes que todos los números impares. 
# Se debe mantener el orden relativo de los elementos originales. 
# Por ejemplo: `anteponer_pares([3,5,2,6,18,7,40,11])` → `[2,6,18,40,3,5,7,11]`

# Escribir el codigo debajo de esta linea

def anteponer_pares(lista):

    lista_pares = []
    lista_impares = []

    for i in range(len(lista)):

        if lista[i]%2 == 0:
            lista_pares.append(lista[i])
        else:
            lista_impares.append(lista[i])
    
    return lista_pares + lista_impares

# Pruebas
assert anteponer_pares([3,5,2,6,18,7,40,11]) == [2,6,18,40,3,5,7,11]