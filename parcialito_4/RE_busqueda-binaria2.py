def _busqueda_binaria(lista, elemento, posicion, contador):

    print(lista)

    medio = len(lista) // 2
    posicion = posicion//2
    contador += 1
    if lista[medio] == elemento:
        return (posicion, contador)
    
    elif len(lista) == 1:
        return (posicion, lista[0])
    
    elif lista[medio] > elemento:
        return _busqueda_binaria(lista[:medio], elemento, posicion, contador)
    
    elif lista[medio] < elemento:
        return _busqueda_binaria(lista[medio:], elemento, posicion, contador)

def busqueda_binaria(lista, elemento):
    if not lista:
        lista.append(elemento)
        return 0
    posicion = len(lista)    
    contador = 0

    i, n = _busqueda_binaria(lista, elemento, posicion, contador)

    i = i * n
    
    if lista[i] == elemento:
        return i
    
    else:
        lista.insert(lista.index(lista[n]), elemento)
        return lista.index(lista[n])

lista = [1,2,5,7,9,11,14]
print(busqueda_binaria(lista, 2))

print(lista)