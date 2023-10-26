# Escribir una funcion que reciba una palabra 
# y devuelva una lista con todas las rotaciones
# de esa palabra. Por ejemplo, si recibe: ’rotar’, debe devolver:

# [’rotar’,’otarr’,’tarro’,’arrot’,’rrota’]

def rotaciones(cadena):
	rotaciones = []                                         #creo una lista vacia para meter las rotaciones.
	for i in range(len(cadena)):                            #el largo de la palabra nos da la cantidad de rotaciones que va a haber
		rotaciones.append(cadena[i:] + cadena[:i])          #para rotar tomo los caracteres desde el i y los sumo con los que hay antes del i
	return rotaciones