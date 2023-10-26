# Escribir una función que recibe una cadena y un numero n 
# y devuelve la cadena eliminando los caracteres en todas 
# las posiciones multiplos de n, contando las posiciones desde 1.
# Ejemplo: con la cadena 'abcdefghijk' y n=3 debe devolver 'abdeghjk'

# Escribir debajo de este comentario el código del ejercicio

def eliminar_multiplos(cadena, n):

    contador = 1
    resultado = ""

    for caracter in cadena:

        if contador < n:
            resultado += caracter
        
        elif contador%n != 0:
            resultado += caracter
    
        contador += 1
    
    return resultado


# def eliminar_multiplos(cadena, n):
#     letrasnomultiplo=[]
#     letrasenlistadas = list(cadena)
#     for i in range(1,len(letrasenlistadas)+1):
#         if i%n != 0:
#             letrasnomultiplo.append(letrasenlistadas[i-1])
#     return "".join(letrasnomultiplo)



# Pruebas
assert eliminar_multiplos('abcdefghijk', 3) == 'abdeghjk'
assert eliminar_multiplos('abcdefghijk', 12) == 'abcdefghijk'
