# 3. Escribir una función `ajustar_linea()` que recibe una cadena y un número `n`, 
# y devuelva una lista con la cadena original partida en multiples cadenas de tamaño `n`.
# La unica cadena con tamaño menor a `n` es la ultima (si no hay suficientes caracteres).
# Ejemplos:
# ajustar_linea('Algoritmos', 5)
#   => ['Algor', 'itmos']
# ajustar_linea('Algoritmos y programacion I', 8)
#   => ['Algoritm', 'os y pro', 'gramacio', 'n I']


# Completar la siguiente funcion
def ajustar_linea(cadena, n):
    resultado = []
    for i in range(n,len(cadena)+1,n):
        cadenita = cadena[i-n:i]
        resultado.append(cadenita)

    if len(cadena)%n != 0:
        resultado.append(cadena[len(cadena) - len(cadena)%n:])
    
    print(resultado)
    return resultado


assert ajustar_linea('Algoritmos', 5) == ['Algor', 'itmos']
assert ajustar_linea('Algoritmos y programacion I', 8) == ['Algoritm', 'os y pro', 'gramacio', 'n I']