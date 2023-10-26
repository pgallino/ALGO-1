"""Ejercicio 126 pilas

Se está organizando una fiesta y se conoce la hora de entrada y salida de los N invitados.

A cada invitado se le asigna uno de los 3 espacios que hay para estacionar.

Cada espacio tiene el ancho de un auto pero el largo de varios, por lo que cada auto que llega bloquea a los que ya estaban previamente.

Hacer una función que dada una lista con tuplas (<hora>,<entra/sale>,<invitado>,<espacio>) que están ordenadas por hora, indique si la asignación de espacios es válida.

Una asignación es inválida si algún invitado no puede salir a su horario designado porque hay otro auto bloqueándole la salida.

Ejemplo: [(21,ENTRA,"Blas",2), (22,ENTRA,"Ailín",2), (23.5,SALE,"Blas",2), (24,SALE,"Ailín",2)] 

no es una asignación válida porque el auto de Ailín no deja salir a Blas a horario. 

En cambio ésta sí es válida: [(21,ENTRA,"Blas",2), (22,ENTRA,"Ailín",2), (23,SALE,"Ailín",2), (23.5,SALE,"Blas",2)]."""

from Pila import Pila
from Cola import Cola

def indicar_estacionamiento(lista_tuplas):

    orden_entrada_1 = Pila()
    orden_salida_1 = Cola()
    orden_entrada_2 = Pila()
    orden_salida_2 = Cola()
    orden_entrada_3 = Pila()
    orden_salida_3 = Cola()

    for i in range(len(lista_tuplas)):

        if lista_tuplas[i][1] == "ENTRA":
            if lista_tuplas[i][3] == 1:
                orden_entrada_1.apilar(lista_tuplas[i][2])
            
            elif lista_tuplas[i][3] == 2:
                orden_entrada_2.apilar(lista_tuplas[i][2])
            
            elif lista_tuplas[i][3] == 3:
                orden_entrada_3.apilar(lista_tuplas[i][2])

        elif lista_tuplas[i][1] == "SALE":
            if lista_tuplas[i][3] == 1:
                orden_salida_1.encolar(lista_tuplas[i][2])
            
            elif lista_tuplas[i][3] == 2:
                orden_salida_2.encolar(lista_tuplas[i][2])
            
            elif lista_tuplas[i][3] == 3:
                orden_salida_3.encolar(lista_tuplas[i][2])

    while not orden_salida_1.esta_vacia() and not orden_entrada_1.esta_vacia():
        actual_s = orden_salida_1.desencolar()
        actual_e = orden_entrada_1.desapilar()
        if actual_e != actual_s:
            return False
    
    while not orden_salida_2.esta_vacia() and not orden_entrada_2.esta_vacia():
        actual_s = orden_salida_2.desencolar()
        actual_e = orden_entrada_2.desapilar()
        if actual_e != actual_s:
            return False
    
    while not orden_salida_3.esta_vacia() and not orden_entrada_3.esta_vacia():
        actual_s = orden_salida_3.desencolar()
        actual_e = orden_entrada_3.desapilar()
        if actual_e != actual_s:
            return False
    
    return True

secuencia_1 = [(21,"ENTRA","Blas", 2), (22,"ENTRA","Ailín",2), (23.5,"SALE","Blas",2), (24,"SALE","Ailín",2)]
print(indicar_estacionamiento(secuencia_1))
secuencia_2 = [(21,"ENTRA","Blas",2), (22,"ENTRA","Ailín",2), (23,"SALE","Ailín",2), (23.5,"SALE","Blas",2)]
print(indicar_estacionamiento(secuencia_2))




    

    
