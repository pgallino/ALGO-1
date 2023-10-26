def temperaturas_maximas(ruta):
    # HACER: implementar la función
    diccionario = {}
    with open(ruta) as archivo:

        for linea in archivo:
            
            linea = linea.rstrip("\n").split(",")

            if len(linea) != 3:
                continue
            
            fecha , lugar, temperatura = linea

            temperatura = int(temperatura)

            if -72 > temperatura > 57: #mínima y máxima temperatura registrada en la tierra.
                continue

            fecha_analisis = fecha.split("-") #verifico que la fecha sea posible.

            if len(fecha_analisis[0]) != 4 or len(fecha_analisis[1]) != 2 or len(fecha_analisis[2]) != 2 :
                continue

            fecha_maxima, temperatura_maxima = diccionario.get(lugar, (None,0))

            if temperatura > temperatura_maxima:
                temperatura_maxima = temperatura
                fecha_maxima = fecha
                diccionario[lugar] = (fecha_maxima,temperatura_maxima)
        
        return diccionario


def pruebas():
    # El archivo temperaturas.csv contiene:
    #
    # 2021-08-30,Buenos Aires,22
    # 021-08-29,Buenos Aires,24
    # 2021-08-27,22
    # 2021-08-31,Buenos Aires,23
    # 2021-08-30,La Plata,20
    # 2021-08-31,La Plata,19
    # 2021-08-29,La Plata,21,
    #
    # Notar que algunas líneas no cumplen con el formato y deben ser ignoradas.

    assert temperaturas_maximas("temperaturas.csv") == {
        "Buenos Aires": ("2021-08-31", 23),
        "La Plata": ("2021-08-30", 20),
    }

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()

