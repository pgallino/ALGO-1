"""Ejercicio 163 recursion
Implementar el algoritmo de búsqueda binaria de manera recursiva."""

def busqueda_binaria(lista, elemento):
    print(lista)
    medio = len(lista) // 2
    if lista[medio] == elemento:
        return True
    
    elif len(lista) == 1:
        return False
    
    elif lista[medio] > elemento:
        return busqueda_binaria(lista[:medio], elemento)
    
    elif lista[medio] < elemento:
        return busqueda_binaria(lista[medio:], elemento)


print(busqueda_binaria([1,2,3,4,5,6,7,8,9,10,14,16,19,433,912,4221,5123], 14))

