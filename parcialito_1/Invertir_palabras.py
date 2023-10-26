"""escribir una funcion que invierta las palabras"""

def invertir_palabras(frase):

    frase = frase.split(" ")

    for i in range(len(frase)):
        frase[i] = (frase[i])[::-1]
    
    
    return " ".join(frase)