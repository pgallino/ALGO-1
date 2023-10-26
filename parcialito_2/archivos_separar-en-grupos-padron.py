"""Se tiene una lista de los alumnos de una materia y se desea dividirlos en 3 grupos según resto del cociente entre el padrón del alumno y 3.

Si el padrón es $12345$, se deberá hacer $12345 % 3 = 2$
Si el padrón es $7774$ se deberá hacer $7774 % 3 = 1$
Si el padrón es $36$ se deberá hacer $36 % 3 = 0$
La lista de los alumnos se encuentra en un archivo que tiene un número de padrón por línea. 
Se pide escribir una función que reciba por parámetro el nombre del archivo de alumnos y devuelva 3 archivos cuyos nombres tendrán el formato:

 <nombre archivo alumnos>_Enunciado<número de grupo>.txt con la lista de padrones correspondientes a cada grupo uno por línea.

Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos deben quedar cerrados."""

def separar_en_grupos(ruta_archivo, ruta_grupo1, ruta_grupo2, ruta_grupo3):

    with open(ruta_archivo) as archivo, open(ruta_grupo1, "w") as grupo1, open(ruta_grupo2,"w") as grupo2, open(ruta_grupo3, "w") as grupo3:
        
        grupo1.write("Grupo número 1\n")
        grupo2.write("Grupo número 2\n")
        grupo3.write("Grupo número 3\n")

        for linea in archivo:
            linea = int(linea.rstrip("\n"))
            if linea%3 == 1:
                grupo1.write(f"{linea}\n")
            elif linea%3 == 2:
                grupo2.write(f"{linea}\n")
            elif linea%3 == 0:
                grupo3.write(f"{linea}\n")