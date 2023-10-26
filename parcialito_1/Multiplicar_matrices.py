"""Escribir una función que reciba dos matrices y devuelva el producto. Las matrices están representadas como listas de listas.

Por ejemplo, para el siguiente producto:

[ 2 3 ] . [ 5 7 ] = [ 16 17 ]
[ 1 9 ]   [ 2 1 ] = [ 23 16 ]
Se tiene la siguiente invocación:

>>> multiplicar_matrices([[2, 3], [1, 9]], [[5, 7], [2, 1]])
[[16, 17], [23, 16]]"""



def multiplicar_matrices(m1, m2):

    resultado = []
    for i in range(len(m1)):

        sublista = []

        for j in range(len(m2[0])):
            
            sublista.append((m1[i][0] * m2[0][j]) + (m1[i][1] * m2[1][j]))

        resultado.append(sublista)
    
    return resultado

print(multiplicar_matrices([[1,2],[3,4],[5,6]], [[1,2,3],[3,4,5]]))