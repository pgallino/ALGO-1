"""Ejercicio 2.8. Escribir un programa que tome una cantidad m de valores ingresados por el usua-
rio, a cada uno le calcule el factorial (utilizando la función escrita en el ejercicio 1.5) e imprima el resultado junto con el número de orden correspondiente."""

import factorial

def factoriales():
    lista=[]
    lista2=[]
    while True:
        numero = input("ingrese el numero: ")
        lista2.append(numero)
        if numero != "":
            facto = factorial.factorial(int(numero))
            lista.append(facto)
        if numero == "":
            break
    for i in range(0,len(lista)):
        factorialvalor=lista[i]
        valor=lista2[i]
        print(f"el factorial de {valor} es {factorialvalor}")

factoriales()
    
        
