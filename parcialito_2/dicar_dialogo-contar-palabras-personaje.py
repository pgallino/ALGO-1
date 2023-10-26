'''
    Se tiene un archivo de texto que contiene un díálogo entre una cantidad de personas
desconocida, de manera que cada línea del archivo tiene este formato

Persona1: una frase de cierta cantidad de palabras
Persona2: otra frase de cierta cantidad de palabras
Persona1: volviendo a hablar
PersonaN: apareciendo con una frase de cierta cantidad de palabras
(asumir que las frases contienen únicamente palabras, no contienen signos de puntuacion,
ni numeros, ni ningun caracter que no sean letras o espacios).

Escribir una funcion que reciba la ruta a un archivo de este tipo y devuelva
cuantas veces dijo cada palabra cada una de las personas involucradas en el díalogo
(es decir, debe devolver un diccionario con el siguiente formato:

{ Persona1: { palabra_1: cant_1, palabra_2: cant_2 }, Persona2: { ... } .. }
    '''

def leer_dialogo(nombre_archivo):

    with open(nombre_archivo) as archivo:

        diccionario_personajes = {}

        for linea in archivo:
            fila = linea.replace(":","").rstrip("\n")
            palabras = fila.split()
            personaje = palabras.pop(0)
            diccionario_personajes[personaje] = diccionario_personajes.get(personaje, {})

            for palabra in palabras:
                diccionario_personajes[personaje][palabra] = diccionario_personajes[personaje].get(palabra, 0) + 1

        return diccionario_personajes