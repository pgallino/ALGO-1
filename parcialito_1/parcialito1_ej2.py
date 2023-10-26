# Escribir una funcion `dar_vuelta` que reciba una lista de tuplas de numeros y que 
# devuelva una nueva lista de tuplas, donde la primer tupla tendra el primer elemento 
# de todas las tuplas originales; la segunda, los segundos, etc.

# Ejemplo: 
# [(1,2,3), (4,5), (6,), (7,8,9,10)]
#   => 
# [(1,4,6,7), (2,5,8), (3,9), (10,)]

# Nota: las tuplas originales no tienen todas la misma cantidad de elementos entre sí.
# Ayuda: Una tupla de un solo elemento se puede crear de la forma `t = (elem,)`

# Escribir debajo de este comentario el código del ejercicio

def dar_vuelta(lista):

    resultado = []

    maxima_longitud = max(list(map(len, lista)))

    for i in range(maxima_longitud):

        sublista = []

        for j in range(len(lista)):

            if i > len(lista[j]) - 1:
                continue

            sublista.append(lista[j][i])
        
        resultado.append(sublista)
    
    return list(map(tuple, resultado))



# Pruebas

l_inicial = [(1,2,3), (4,5), (6,), (7,8,9,10)]
l_esperada = [(1,4,6,7), (2,5,8), (3,9), (10,)]
l_resultado = dar_vuelta(l_inicial)

for i in range(len(l_esperada)):
    assert list(l_esperada[i]) == list(l_resultado[i])
