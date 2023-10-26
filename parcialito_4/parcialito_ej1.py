# Escribir una funcion recursiva que dada una cadena le haga un "flip" de mayúsculas, 
# es decir, que devuelva una nueva cadena con los caracteres en minúscula transformados a mayúscula y 
# los caracteres en mayúscula transformados en minúscula.

#Escribir el código debajo de esta linea

def flip_mayusculas(cadena):
    
    if not cadena:
        return ""
    
    if cadena[-1] in "abcdefghijklmnopqrstuvwxyz":
        caracter = cadena[-1].upper()
        
        return flip_mayusculas(cadena[:-1]) + caracter
    
    elif cadena[-1] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        caracter = cadena[-1].lower()

        return flip_mayusculas(cadena[:-1]) + caracter
    
    else:

        caracter = cadena[-1]
        return flip_mayusculas(cadena[:-1]) + caracter



# Pruebas
cadena = "AlgoRitmOs Y ProGramAcion 1"
resultado = 'aLGOrITMoS y pROgRAMaCION 1'
assert flip_mayusculas(cadena) == resultado