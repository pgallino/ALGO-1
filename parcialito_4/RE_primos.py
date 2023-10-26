"""Realizar una función recursiva que reciba una lista de Python de números y

devuelva una nueva lista eliminando los dígitos que son sucedidos por un número primo, 

devolviendo una lista igual a la recibida por parámetro pero sin los dígitos que cumplan la condición especificada. 

Nota: la función es_primo() ya se encuentra implementada.

Ejemplo: eliminar_sucedidos_primo([4,7,6,11,13]) → [7,13]"""

def esprimo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def eliminar_no_primos(lista):  #no es lo que se pide, borra los primos
    
    if not lista:
        return lista
    
    elif esprimo(lista[-1]):
        return eliminar_no_primos(lista[:-1]) + [lista[-1]]
    
    elif esprimo(lista[-1]) == False:
        return eliminar_no_primos(lista[:-1])

print(eliminar_no_primos([4,7,6,11,13]))

def _eliminar_sucedidos_primo(lista, anterior):

    if not lista:
        return lista

    elif esprimo(anterior):
        anterior = lista[-1]
        return _eliminar_sucedidos_primo(lista[:-1], anterior)
    
    elif not esprimo(anterior):
        anterior = lista[-1]
        return _eliminar_sucedidos_primo(lista[:-1], anterior) + [anterior]

def eliminar_sucedidos_primo(lista):
    anterior = lista[-1]
    return _eliminar_sucedidos_primo(lista, anterior) + [anterior]

print(eliminar_sucedidos_primo([4,7,6,11,13]))

        