"""Se tienen dos archivos cuyos campos son DNI,Apellido,Nombre, y están ordenados por DNI. 

Escribir una función que reciba los nombres de dos archivos como los mencionados,

y genere un nuevo archivo que incluya los datos de ambos archivos de entrada, también ordenados por DNI y sin duplicados.

Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos deben quedar cerrados."""

def unir_archivos_ordenados1(ruta_archivo_1, ruta_archivo_2, archivo_total): #si entra en la memoria

    with open(ruta_archivo_1) as archivo1, open(ruta_archivo_2) as archivo2, open(archivo_total, "w") as archivo_total:

        lista_tuplas = []

        for linea in archivo1:
            dni, apellido, nombre = linea.rstrip("\n").split(",")
            tupla = (int(dni),apellido,nombre)
            if not tupla in lista_tuplas:
                lista_tuplas.append(tupla)
        
        for linea in archivo2:
            dni, apellido, nombre = linea.rstrip("\n").split(",")
            tupla = (int(dni),apellido,nombre)
            if not tupla in lista_tuplas:
                lista_tuplas.append(tupla)
        
        dni_ordenados = sorted(lista_tuplas)
        for tupla in dni_ordenados:
            dni, apellido, nombre = tupla
            archivo_total.write(f"{dni},{apellido},{nombre}\n")




def unir_archivos_ordenados2(ruta_archivo_1, ruta_archivo_2, archivo_total): #si no entra en la memoria

    with open(ruta_archivo_1) as archivo1, open(ruta_archivo_2) as archivo2, open(archivo_total, "w") as archivo_total:

        linea1 = archivo1.readline()
        dni1,apellido1,nombre1 = linea1.rstrip("\n").split(",")

        linea2 = archivo2.readline()
        dni2,apellido2,nombre2 = linea2.rstrip("\n").split(",")

        linea_mas_corta = 0

            
        while True:

            if int(dni1) > int(dni2):
                archivo_total.write(linea2)
                linea2 = archivo2.readline()
                if not linea2:
                    linea_mas_corta += 1
                    archivo_total.write(linea1)
                    break
                else:
                    dni2,apellido2,nombre2 = linea2.rstrip("\n").split(",")

            elif int(dni1) < int(dni2):
                archivo_total.write(linea1)
                linea1 = archivo1.readline()
                if not linea1:
                    linea_mas_corta += 2
                    archivo_total.write(linea2)
                    break
                else:
                    dni1,apellido1,nombre1 = linea1.rstrip("\n").split(",")

            elif int(dni1) == int(dni2):

                archivo_total.write(linea1)
                linea1 = archivo1.readline()
                linea2 = archivo2.readline()
                if not linea1 or not linea2:
                    if not linea1:
                        linea_mas_corta += 2
                    else:
                        linea_mas_corta += 1
                    break
                else:
                    dni2,apellido2,nombre2 = linea2.rstrip("\n").split(",")
                    dni1,apellido1,nombre1 = linea1.rstrip("\n").split(",")

        if linea_mas_corta == 1:
            archivo_total.write(linea1)
        elif linea_mas_corta == 2:
            archivo_total.write(linea2)

        while True:
        
            if linea_mas_corta == 1:
                linea1 = archivo1.readline()
                if not linea1:
                    break
                else:
                    dni1,apellido1,nombre1 = linea1.rstrip("\n").split(",")
                    archivo_total.write(linea1)

            elif linea_mas_corta == 2:
                linea2 = archivo2.readline()
                if not linea2:
                    break
                else:
                    dni2, apellido_i, nombre_i = linea2.rstrip("\n").split(",")
                    archivo_total.write(linea2)
            


            





            

                