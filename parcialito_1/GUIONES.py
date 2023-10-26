"""Escribir un programa que le pida al usuario que ingrese un número entero positivo n y una cadena, e imprima la misma cadena pero con un guión (-) cada n lugares.

Ejemplo: n = 2, cadena = Otra frase devuelta; debe imprimir Es-to- e-s -un- e-je-mp-lo-.

Ingrese una frecuencia: 2
Ingrese una frase: Esto es un ejemplo.
Es-to- e-s -un- e-je-mp-lo-.
Otro ejemplo: n = 1, cadena = Otra frase devuelta; debe imprimir O-t-r-a- -f-r-a-s-e- -d-e-v-u-e-l-t-a

Ingrese una frecuencia: 1
Ingrese una frase: Otra frase devuelta
O-t-r-a- -f-r-a-s-e- -d-e-v-u-e-l-t-a"""

def pedir_numero_cadena():

    frecuencia = int(input("Ingrese una frecuencia: "))
    frase = input("Ingrese una frase: ")
    contador = 0
    resultado = ""

    for i in range(len(frase)):

        if contador == frecuencia - 1:

            resultado += (frase[i] + "-")

            contador = 0
        
        else:

            resultado += frase[i]
            contador += 1
    
    if resultado[-1] == "-":
        print(resultado[:-1])
    
    else:
        print(resultado)

pedir_numero_cadena()