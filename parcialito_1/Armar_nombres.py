def escribir_nombres(lista):

    resultado = []

    for i in range(len(lista)):
        if i == len(lista):
            valor = lista[i][1] + " " + lista[i][2] + ". " + lista[i][0] + ", "
        else:
            valor = lista[i][1] + " " + lista[i][2] + ". " + lista[i][0]

        resultado.append(valor)
    
    return resultado