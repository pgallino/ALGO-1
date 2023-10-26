"""Dado el nombre del archivo en el que están listadas las materias de la facultad con el formato:

dd.cc - nombre de materia

en dónde dd es el número del departamento y cc es el número de la materia,

se pide escribir una función que devuelva un diccionario que asocie códigos de departamento con una lista de los nombres de las materias del departamento.

Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos deben quedar cerrados."""

def juntar_departamentos_materias(ruta_archivo):

    diccionario = {}
    with open(ruta_archivo) as archivo:

        for linea in archivo:
            linea = linea.rstrip("\n").split(" - ")
            codigos = linea[0].split(".")
            codigo_departamento = codigos[0]
            diccionario[codigo_departamento] = diccionario.get(codigo_departamento, []) + [linea[1]]
            
    return diccionario
