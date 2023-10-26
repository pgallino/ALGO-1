"""Escribir una función que reciba una cantidad de iteraciones de una tirada de 2 dados a realizar y 

devuelva la cantidad de veces que se observa cada valor de la suma de los dos dados.

Nota: utilizar el módulo random para obtener tiradas aleatorias.

Algunos posibles resultados:

>>> contar_resultados_dados(1)
{3: 1, 5: 1}
>>> contar_resultados_dados(1)
{4: 2}
>>> contar_resultados_dados(3)
{2: 1, 5: 1, 4: 2, 6: 1, 3: 1}
>>> contar_resultados_dados(3)
{6: 1, 4: 2, 3: 2, 5: 1}
>>> contar_resultados_dados(3)
{1: 2, 2: 2, 6: 1, 3: 1}"""

import random

# La siguiente línea de código hace que random.randint siempre genere la misma secuencia de números.
# Es necesaria para que cada vez que se corran las pruebas se obtengan los mismos resultados. En un programa "real" no debería estar. 
random.seed(123)

def contar_resultados_dados(n):

    tiradas = {}

    for i in range(n):
        numero = random.randint(1,6)
        tiradas[numero] = tiradas.get(numero, 0) + 1
    
    return tiradas