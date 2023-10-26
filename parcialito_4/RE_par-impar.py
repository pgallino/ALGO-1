"""hacer la funcion par e impar con recursividad cruzandolas, si el anterior al numero es impar, el numero es par y viceversa
se sabe que el 1 es impar"""


def par(n):

    if n == 1:
        return False

    return impar(n-1)



def impar(n):

    if n == 1 :
        return True 
    return par (n-1)


"""explicación: Si el numero es par, y lo meto en par(), al llegar al 1 cae en la funcion impar(), entonces devuelve True.
si el numero es impar y lo meto en par(), al llegar al 1 cae en la funcion par(), entonces devuelve False.

si el numero es impar y lo meto en impar(), al llegar al 1 cae en la funcion impar(), entonces devuelve True.
si el numero es par y lo meto en impar(), al llegar al 1 cae en la funcion par(), entonces devuelve False."""