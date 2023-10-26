"""Se dispone de un archivo .csv sin encabezado. Se desconoce el total de columnas del mismo, pero se sabe que:

En la segunda columna se encuentran nombres de libros.
En la tercer columna, los autores que los escribieron. Si lo escribió más de un autor, estarán separados por el caracter -.
Por lo que el archivo tendrá la forma: [ Columna1 ,NombreLibro, Autores, Columna4 , … , ColumnaN ]

Escribir una función que reciba el nombre de dicho archivo 
y devuelve un diccionario donde la clave sea un autor y el valor asociado una lista con los nombres de los libros escritos por el mismo.

Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos deben quedar cerrados."""

def relacionar_autores_libros(ruta_archivo):
    diccionario = {}
    with open(ruta_archivo) as archivo:
        diccionario = {}
        for linea in archivo:
            linea = linea.rstrip("\n").split(",")
            lista_autores = linea[2].split("-")
            for autor in range(len(lista_autores)):
                clave = lista_autores[autor]
                diccionario[clave] = diccionario.get(clave, []) + [linea[1]]
    return diccionario
