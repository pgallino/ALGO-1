def transponer(m):
    # HACER: implementar la funcion
    resultado = []
    for n in range(len(m[0])):
        resultado.append([])

    for i in range(len(m)):
        for j in range(len(m[0])):
            resultado[j].append(m[i][j])
    
    return resultado

def pruebas():
    m = [
        [1, 2],
        [3, 4],
        [5, 6],
    ]

    mt = transponer(m)

    assert mt == [
        [1, 3, 5],
        [2, 4, 6],
    ]

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
