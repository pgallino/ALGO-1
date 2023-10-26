def insertar_entre_letras(cadena, caracter):
    '''
    DOC: inserta el caracter entre cada letra de la cadena original.
    '''
    resultado = ''

    for c in cadena:
        resultado += c + caracter

    return resultado[:-1]


def reemplazar_espacios(cadena, caracter):
    '''
    DOC: reemplaza todos los espacios de la cadena original por el caracter.
    '''
    return caracter.join(cadena.split(" "))


def reemplazar_digitos(cadena, caracter):
    '''
    DOC: reemplaza los digitos de la cadena por el caracter
    '''
    digitos="1234567890"
    for digitos in digitos:
        cadena = cadena.replace(digitos,caracter)
    return cadena