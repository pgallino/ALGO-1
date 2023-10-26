def consonantes(cadena):
    '''
    DOC: Devuelva solamente las letras consonantes.
    '''
    resultado = ""
    for c in cadena:
        if c in " bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTWXYZ":
            resultado += c
    return resultado



def vocales(cadena):
    '''
    DOC: Devuelva solamente las letras vocales.
    '''
    resultado = ""
    for c in cadena:
        if c in " aeiouAEIOU":
            resultado += c
    return resultado


def avanzar_vocales(cadena):
    '''
    DOC: Reemplace cada vocal por su siguiente vocal.
    '''
    resultado = ""
    for c in cadena:
        if c in "bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTWXYZ":
            resultado += c
        if c in "a":
            resultado += "e"
        if c in "e":
            resultado += "i"
        if c in "i":
            resultado += "o"
        if c in "o":
            resultado += "u"
        if c in "u":
            resultado += "a"
        if c in "A":
            resultado += "E"
        if c in "E":
            resultado += "I"
        if c in "I":
            resultado += "O"
        if c in "O":
            resultado += "U"
        if c in "U":
            resultado += "A"
    return resultado