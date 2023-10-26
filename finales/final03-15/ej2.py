#
# HACER: implementar la funcion
#

def obtener_nombre_popular(ruta):

    resultado_global = {}
    anio_anterior = 0

    with open(ruta) as archivo:

        for linea in archivo:
            
            linea = linea.rstrip("\n").split(";")

            if not linea[0] or not linea[1] or not linea[2]:
                continue

            fecha, apellido, nombre = linea
            
            anio = int(fecha.split("-")[0])

            if anio != anio_anterior and anio_anterior != 0:

                maximo_anio = 0

                for clave in resultado_anio:
                    if resultado_anio[clave] > maximo_anio:
                        maximo_anio = resultado_anio[clave]
                        maximo_nombre = clave
                    

                resultado_global[anio_anterior] = maximo_nombre

                resultado_anio = {}
                
                anio_anterior = anio
            
            elif anio != anio_anterior and anio_anterior == 0:

                anio_anterior = anio
                resultado_anio = {}
            
            if not " " in nombre:
                resultado_anio[nombre.lower()] = resultado_anio.get(nombre.lower(), 0) + 1

            if " " in nombre:
                nombre = nombre.split(" ")

                for i in range(len(nombre)):
                    resultado_anio[nombre[i].lower()] = resultado_anio.get(nombre[i].lower(), 0) + 1
        
        maximo_anio = 0

        for clave in resultado_anio:
            if resultado_anio[clave] > maximo_anio:
                maximo_anio = resultado_anio[clave]
                maximo_nombre = clave
        
        resultado_global[anio_anterior] = maximo_nombre


    
    return resultado_global




def pruebas():

    # creamos un archivo de prueba nacimientos.csv
    with open('nacimientos.csv', 'w') as f:
        f.write('\n'.join([s.strip() for s in """
            1980-01-21;Browning;Lucille Kimora
            1980-12-20;Carey;Caitlyn
            1980-09-05;CHERRY;JANIAH CAITLYN
            1980-03-12;Graves;Serenity
            1980-04-07;Melendez;Essence
            1980-03-05;;
            1980-07-09;MOLINA SHAH;LUZ
            1981-04-25;Barron;Jacqueline
            1981-07-28;CARR;JANESSA
            ;Bryan;Evelin
            1981-08-15;Esparza;Linda Elise
            1981-07-15;Lucas;Chanel
            1981-10-13;mcdowell knight;jacqueline jordin
            1981-01-03;Pineda;Kinley
        """.split('\n')]))

    #
    # HACER: llamar a la función, y verificar con assert el valor devuelto
    # Los nombres más populares son: Caitlyn en 1980 y Jacqueline en 1981.
    #

    diccionario = obtener_nombre_popular("nacimientos.csv")
    print(diccionario)

    assert diccionario[1980] == "caitlyn"
    assert diccionario[1981] == "jacqueline"

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
