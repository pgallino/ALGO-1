# Escribir una función que reciba un número entero n, y devuelva una matriz triangular superior de dimensión n x n, en forma de lista de listas, 
# cuyos elementos son los números del 1 a K en orden (siendo K la cantidad total de números a colocar). 
# Por ejemplo, para n = 4, debe devolver la siguiente matriz:
# [[1, 2, 3, 4],
#  [0, 5, 6, 7],
#  [0, 0, 8, 9],
#  [0, 0, 0, 10]]

# Escribir el codigo debajo de esta linea

def triangular_superior(n):

    resultado = []
    relleno = 1
    
    for i in range(n):

        sublista = []

        for j in range(n):

            if i > j:
                sublista.append(0)
            
            else:
                sublista.append(relleno)

                relleno += 1
        
        resultado.append(sublista)
                
    
    return resultado

# Pruebas
resultado_esperado = [[1, 2, 3, 4],[0, 5, 6, 7],[0, 0, 8, 9],[0, 0, 0, 10]]
assert triangular_superior(4) == resultado_esperado