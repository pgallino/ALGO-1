# Escribir un programa que pida al usuario que ingrese líneas de texto, hasta que ingrese una línea vacía.
# El programa deberá imprimir todas las líneas encerradas en un marco.
# Ejemplo:
# Ingrese una linea o enter para terminar: Hola
# Ingrese una linea o enter para terminar: Mundo
# Ingrese una linea o enter para terminar: en un marco
# Ingrese una linea o enter para terminar:
# ***************
# * Hola        *
# * Mundo       *
# * en un marco *
# ***************

# Escribir debajo de este comentario el código del ejercicio
def pedir_entradas_al_usuario():
    entradas = []
    while True:
        entrada = input("Ingrese una linea o enter para terminar: ")
        if not entrada:
            return entradas
        entradas.append(entrada)

def imprimir_enmarcado(entradas):
    longitud_maxima = 0
    for entrada in entradas:
        if len(entrada) > longitud_maxima:
            longitud_maxima = len(entrada)
	
    print("*" * (longitud_maxima + 4))      #es mas cuatro para que queden dos y dos de más a los costados

    for entrada in entradas:
        print(f"* {entrada}{' ' * (longitud_maxima - len(entrada))} *")  #imprime cada entrada con el asterico al principio, mas la cantidad de espacios necesarios y el asterisco final
	
    print("*" * (longitud_maxima + 4))

def main():
    entradas = pedir_entradas_al_usuario()
    imprimir_enmarcado(entradas)

main()
        
        



# Pruebas
import sys
import io
sys.stdin = io.StringIO('Hola\nMundo\nen un marco\n\n')
sys.stdout = io.StringIO()
main()
assert(sys.stdout.getvalue() == 'Ingrese una linea o enter para terminar: Ingrese una linea o enter para terminar: Ingrese una linea o enter para terminar: Ingrese una linea o enter para terminar: ***************\n* Hola        *\n* Mundo       *\n* en un marco *\n***************\n')
sys.stdout = sys.__stdout__
sys.stdin = sys.__stdin__
