# Escribir una funcion que sacuda una matriz, es decir, 
# que rote las filas pares un elemento hacia la derecha,
# y rote las filas impares un elemento hacia la izquierda.
# Esta función debe ser in-place, es decir, debe trabajar sobre la matriz recibida.
# La matriz esta representada como una lista de listas.

# Ejemplo:
# 1 2 3 11    11 1 2 3
# 4 5 6 12 -> 5 6 12 4
# 7 8 9 13    13 7 8 9

# Escribir debajo de este comentario el código del ejercicio

# def sacudir(matriz):
#     for i in range(len(matriz)): 
#         fila = matriz[i]
#         if i % 2 == 0:
#             fila.insert(0, fila.pop())       #si es par, Der. Si tengo que rotar [1,2,3,11] hacia la derecha, tengo que sacar el ultimo y ponerlo primero [11,1,2,3]
#         else:
#             fila.append(fila.pop(0))         #si es impar, izq. Si tengo que rotar [4,5,6,12] hacia la izquierda, tengo que sacar el primero y ponerlo ultimo [5,6,12,4]
#     return matriz


def sacudir(matriz):

    for i in range(len(matriz)):

        if i%2 == 0:
            matriz[i].insert(0, matriz[i].pop())
        
        else:
            matriz[i].append(matriz[i].pop(0))
    
    return matriz



# Pruebas
assert sacudir([[1, 2, 3, 11], [4, 5, 6, 12], [7, 8, 9, 13]]) == [[11, 1, 2, 3], [5, 6, 12, 4], [13, 7, 8, 9]]
assert sacudir([[1, 7], [7, 1], [1, 7]]) == [[7, 1], [1, 7], [7, 1]]
