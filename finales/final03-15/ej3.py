#
# HACER: implementar la funcion
#

def multi_merge(lista):

    if len(lista) == 1:
        return lista

    for i in range(len(lista)-1,0,-1):

        lista1 = lista[i]
        lista2 = lista[i-1]

        i, j = 0, 0
        resultado = []

        while(i < len(lista1) and j < len(lista2)):
            if (lista1[i] < lista2[j]):
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1
        
        resultado += lista1[i:]
        resultado += lista2[j:]

        lista = lista[:-1]

        if len(lista) > 0:
            lista = lista[:-1]
        
        lista.append(resultado)
    
    return lista[0]



def pruebas():
    print(multi_merge([[1, 3, 5, 7, 9], [2, 4, 6, 8],[1,5,8,10],[5,7,8,9]]))
    assert multi_merge([[1, 3, 5, 7, 9], [2, 4, 6, 8],[1,5,8,10],[5,7,8,9]]) == [1,1,2,3,4,5,5,5,6,7,7,8,8,8,9,9,10]
    assert multi_merge([[1, 3, 5, 7, 9], [2, 4, 6, 8]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # OPCIONAL: agregar más casos de prueba. Sugerencias: probar distintos valores de k,
    # y listas de diferentes longitudes (no tienen por qué ser todas de la misma longitud).

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
