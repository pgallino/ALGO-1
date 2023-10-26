def extraer_distritos(todos):
    # HACER: implementar la función
    with open(todos) as archivo:

        for linea in archivo:

            linea = linea.rstrip("\n").split(",")

            comuna, dni = linea

            with open(f"{comuna}.csv", "a+") as archivo_salida:

                archivo_salida.seek(0)
                data = archivo_salida.read(100)
                if len(data) > 0 :
                    archivo_salida.write("\n")
                archivo_salida.write(f"{dni}")
            



def pruebas():
    extraer_distritos("todos.csv")

    # todos.csv contiene:
    # ---------
    # 12,345678
    # 15,456789
    # 12,123456
    # 12,234567
    # 15,123123

    # Se deberían haber creado dos archivos:
    #
    # 12.csv
    # ------
    # 345678
    # 123456
    #
    #
    # 15.csv
    # ------
    # 456789
    # 234567
    # 123123

    from os import path
    print(f"{path.basename(__file__)}: OK (verificar que se hayan creado los archivos)")

pruebas()
