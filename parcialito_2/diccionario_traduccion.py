"""Escribir una función traducir_a_ingles, que recibe una cadena a traducir y 

un diccionario cuyas claves son palabras en español y el valor asociado a cada una es su traducción al inglés, 

y devuelva la cadena traducida. En caso que una palabra de la cadena no se encuentre en el diccionario, la función debe incluir la palabra sin traducir. 

Asumir que todas las palabras, tanto de la cadena como las del diccionario, están en minúscula."""

def traducir_a_ingles(cadena, diccionario):
    cadena_traducida = []
    for palabra in cadena.lower().split():
        cadena_traducida.append(diccionario.get(palabra, palabra))
    return " ".join(cadena_traducida)

