
#hacer función que reciba una cadena y devuelva todas las palabras capitalizadas

def capitalizar(cadena):
	palabras_capitalizadas = []                             #creo lista vacia para meter las palabras capitalizadas
	for palabra in cadena.split():                                                      #para cada palabra puesta en la lista cadena.split() (lista con las palabras como elementos)
		palabras_capitalizadas.append(palabra[0].upper() + palabra[1:])                  #le uppeo el primer caracter a cada palabra y le sumo el resto de la palabra, y cada una la meto en la lista de palabras capitalizadas
	return " ".join(palabras_capitalizadas)                                              #joineo con espacio la lista con las palabras arregladas formando la misma cadena pero capitalizada



def primeras_letras(cadena):
    '''
    La primera letra de cada palabra.
    '''
    primera_letra=[]
    for palabra in cadena.split(" "):
        primera_letra.append(palabra[0])
    return "".join(primera_letra)



def primera_letra_mayus(cadena):
    '''
    Dicha cadena con la primera letra de cada palabra en mayúsculas
    '''
    mayupalabra=[]
    for palabra in cadena.split(" "):
        mayupalabra.append(palabra[0].upper() + palabra[1:])
    return " ".join(mayupalabra)


def comienzan_con_a(cadena):
    '''
    Las palabras que comiencen con la letra ‘A’ (en mayúsculas o minúsculas).
    '''
    palabra_a=[]
    for palabra in cadena.split(" "):
        if palabra[0] in "Aa":
            palabra_a.append(palabra)
    return " ".join(palabra_a)