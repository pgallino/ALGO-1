"""Ejercicio 164 recursion
Implementar la función merge en forma recursiva. La función recibe dos listas ordenadas y devuelve una lista con los elementos intercalados ordenadamente."""

def merge(lista1, lista2, resultado):

    if not lista1 and not lista2:
        return resultado

    elif not lista1:
        return resultado + lista2
    
    elif not lista2:
        return resultado + lista1
    
    elif lista1[0] > lista2[0]:
        resultado += [lista2[0]]
        return merge(lista1, lista2[1:], resultado)
    
    elif lista1[0] < lista2[0]:
        resultado += [lista1[0]]
        return merge(lista1[1:], lista2, resultado)
    
    else:
        resultado += [lista1[0]]
        resultado += [lista2[0]]
        return merge(lista1[1:], lista2[1:], resultado)

def _merge(lista):

    resultado = []

    if len(lista) < 2:
        return lista
    lista1 = lista[(len(lista)//2):]
    lista2 = lista[:(len(lista)//2)]

    der = _merge(lista1)
    izq = _merge(lista2)
    return merge(izq, der, resultado)


print(_merge([1,5,1,3,8,2,98,21,4,6,2,6,8,2,42,-1,-8]))