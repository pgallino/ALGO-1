"""Escribir una función que reciba dos matrices y devuelva la suma. Las matrices están representadas como listas de listas.

Por ejemplo, para la siguiente suma:

[ 2 3 ] + [ 5 7 ] = [ 7 10 ]
[ 1 9 ]   [ 2 1 ] = [ 3 10 ]
Se tiene la siguiente invocación:

>>> sumar_matrices([[2, 3], [1, 9]], [[5, 7], [2, 1]])
[[7, 10], [3, 10]]"""

def sumar_matrices(m1, m2):
    
    resultado = []
    for i in range(len(m1)):

        sublista = []
        for j in range(len(m1[0])):

            sublista.append(m1[i][j] + m2[i][j])
        resultado.append(sublista)
    
    return resultado