def invertir_lista(lista):

    for i in range(len(lista) // 2):

        lista[i], lista[len(lista) - i - 1] = lista[len(lista) - 1 - i], lista[i]