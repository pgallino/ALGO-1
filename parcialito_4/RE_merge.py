"""Implementar la función merge en forma recursiva. La función recibe dos listas ordenadas y devuelve una lista con los elementos intercalados ordenadamente."""

def _merge(lista1, lista2, resultado):

    if not lista1 and not lista2:
        return resultado

    elif not lista1:
        resultado += lista2
        return resultado
    elif not lista2:
        resultado += lista1
        return resultado
    
    elif lista1[0] > lista2[0]:
        resultado.append(lista2[0])
        return _merge(lista1, lista2[1:], resultado)
    
    elif lista1[0] < lista2[0]:
        resultado.append(lista1[0])
        return _merge(lista1[1:], lista2, resultado)

    elif lista1[0] == lista2[0]:
        resultado.append(lista1[0])
        resultado.append(lista2[0])
        return _merge(lista1[1:], lista2[1:], resultado)

def merge(lista1, lista2):
    resultado = []
    return _merge(lista1, lista2, resultado)


def merge_picada(lista1, lista2):        #esta picada pero ni la entiendo
    if not lista2:      return lista1
    elif not lista1:    return lista2

    if lista1[0] < lista2[0]:
        return [lista1[0]] + merge(lista1[1:], lista2)
    else:
        return [lista2[0]] + merge(lista1, lista2[1:])


merge([1,8],[3,9,10,11,12])