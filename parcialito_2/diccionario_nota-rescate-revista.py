"""Se desea escribir una nota de rescate recortando letras de una revista. 

Escribir una función que reciba por parámetro la nota que se desea escribir y el texto completo de la revista,

 y devuelva True si la revista contiene todas las letras necesarias para escribir la nota (ignorando mayúsculas y minúsculas), False en caso contrario.

Ejemplo: 

Si la revista contiene "Algoritmos y Programacion", podemos escribir la nota "Gracias por la moto", pero no se puede escribir "Porotos amargos" (falta una s)"""

def es_posible_nota_rescate(nota, texto_revista):
    
    letras_revista = {}
    letras_nota = {}

    for caracter in texto_revista.replace(" ","").lower():
        letras_revista[caracter] = letras_revista.get(caracter, 0) + 1

    for caracter in nota.replace(" ","").lower():
        letras_nota[caracter] = letras_nota.get(caracter, 0) + 1

    for clave in letras_nota:
        if not clave in letras_revista or (clave in letras_revista and letras_nota[clave] > letras_revista[clave]):
            return False
    return True
    

