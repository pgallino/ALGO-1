# Escribir una función que pida cadenas al usuario 
# hasta que ingrese una cadena vacı́a.
# Debe devolver una lista de las palabras ingresadas. Por ejemplo:
# Cadena: hola co
# Cadena: mo
# Cadena:  estas ?
# Cadena:
# Debe devolver: [’hola’, ’como’, ’estas’, ’ ?’]

def separar_entrada():
	entradas = ""
	while True:
		entrada = input("Cadena: ")
		if not entrada:                           #o if entrada=="":
			return entradas.split(" ")
		entradas += entrada


#list("hola")=[h, o, l, a]

#"hola".split("")

#si tengo una cadena y la spliteo por espacios consigo todas las palabras en una lista
#si quiero juntar las palabras sin espacio "".join(listadepalabras)