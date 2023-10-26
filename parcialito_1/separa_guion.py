#Escribir un programa que le pida al usuario que ingrese un número entero positivo 
# n y una cadena, e imprima la misma cadena pero con un guión (-) cada n lugares.

# Ejemplo: n = 2, cadena = Otra frase devuelta; debe imprimir 
# Es-to- e-s -un- e-je-mp-lo-.

def insertar_guiones(cadena, n):
	resultado = []
	for i in range(0, len(cadena), n):
		resultado.append(cadena[i:i + n])        #hago una lista donde cada elemento es el contenido de la cadena desde el indice i hasta i+n ya que n corresponde al salto
	return "-".join(resultado)                   #como la tengo separada correctamente en una lista, puedo volverla a hacer cadena con el separador (-)