
"""Ya sabemos que la implementación recursiva del cálculo del número de Fibonacci (Fn = Fn-1 + Fn-2, F0 = 0, F1 = 1)

es ineficiente porque muchas de las ramas calculan reiteradamente los mismos valores.

Escribir una función fibonacci(n) que calcule el enésimo número de Fibonacci de forma recursiva pero que utilice un diccionario

para almacenar los valores ya computados y no computarlos más de una vez.

Nota: Será necesario implementar una función wrapper para cumplir con la firma de la función pedida."""


def _fibonacci(n, diccionario):
    if not n in diccionario:
        valor = _fibonacci(n - 1, diccionario) + _fibonacci(n - 2, diccionario)
        diccionario[n] = valor
    
    return diccionario[n]


def fibonacci(n):
    diccionario = {}
    diccionario[0] = 0
    diccionario[1] = 1
    return _fibonacci(n, diccionario)


"""Fibonacci normal sin diccionario"""

def fib(n):

    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
