# HACER: implementar las funciones

def matriz_guardar(ruta, matriz):

    with open(ruta, "w") as archivo:

        for i in range(len(matriz)):

            lista = list(map(str, matriz[i]))

            lista = "".join(lista)

            archivo.write(lista + "\n")

def matriz_cargar(ruta):

    matriz = []

    with open(ruta) as archivo:

        for linea in archivo:

            if not linea:
                break
            
            else:
                submatriz = []
                linea = linea.rstrip("\n")
                for caracter in linea:
                    submatriz.append(int(caracter))
            
            matriz.append(submatriz)
    
    return matriz


def pruebas():
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
    ]

    # HACER:
    # - llamar a matriz_guardar
    matriz_guardar("matrizguardada.txt",matriz)
    # - llamar a matriz_cargar
    resultado = matriz_cargar("matrizguardada.txt")
    # - verificar que la matriz cargada es idéntica a la original
    assert resultado == matriz

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
