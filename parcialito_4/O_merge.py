"""Ejercicio 174 ordenamiento

a. Dadas dos listas ordenadas de números, implementar una función que reciba estas dos listas 

y devuelva una nueva lista que tenga los elementos de ambas listas ordenados. 

El tiempo de ejecución de la función debe ser lineal (proporcional a la cantidad total de elementos de las dos listas). 

b. ¿En qué famoso algoritmo de ordenamiento se utiliza el algoritmo del punto anterior?"""


#a

def merge(lista1, lista2):

    i = 0
    n = 0
    lista = []

    print(len(lista1))
    print(len(lista2))

    while n != len(lista2) and i != len(lista1):

        if lista1[i] > lista2[n]:

            lista += [lista2[n]]

            n += 1
        
        elif lista1[i] < lista2[n]:

            lista += [lista1[i]]

            i += 1
        
        else:

            lista += ([lista1[i]] + [lista2[n]])

            i += 1
            n += 1


    if n == len(lista2) and i < len(lista1):
        lista += lista1[i:]
        return lista
    
    elif i == len(lista1) and n < len(lista2):
        lista += lista2[n:]
        return lista
    
    else:
        return lista

print(merge([1,3,5,6,8,14,15,16,17],[2,4,5,7,11,13]))

#b se usa en mergesort
    


