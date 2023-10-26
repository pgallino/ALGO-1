from Pila import Pila

'''
    Escribir una función que recibe una expresión matemática (en forma de cadena)
    y devuelve True si los paréntesis ('()'), corchetes ('[]') y llaves ('{}') están correctamente
    balanceados, False en caso contrario.
    '''

def validar(ecuacion):

    pila = Pila()
    tipos = {"]":"[", "}":"{", ")":"("}
    for caracter in ecuacion:
        if caracter in "({[":
            pila.apilar(caracter)
        elif caracter in ")}]" and pila.tope == None:
            return False
        elif caracter in ")}]" and tipos[caracter] == pila.tope.dato:
            pila.desapilar()
        elif caracter in ")}]" and tipos[caracter] != pila.tope.dato:
            return False
    
    return pila.esta_vacia()