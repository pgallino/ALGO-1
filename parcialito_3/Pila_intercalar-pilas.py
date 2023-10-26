"""Ejercicio 130 pilas

EScribir una función intercalar(pilas) que reciba una secuencia de pilas y devuelva una pila con los elementos de todas las pilas intercalados,

manteniendo el orden relativo. Las pilas originales deben quedar vacías. Ejemplo:

intercalar([Pila(1, 2), Pila(3, 4, 5, 6), Pila(7)]) → Pila(1, 3, 7, 2, 4, 5, 6)"""

from Pila import Pila
from Pila import _Nodo

def intercalar_pilas(secuencia):

    pila_intercalada = Pila()
    pila_resultado = Pila()

    vacias = 0

    while vacias != len(secuencia):

        vacias = 0

        for i in range(len(secuencia)):

            if secuencia[i].esta_vacia():
                vacias += 1
                continue
            
            else:
                pila_intercalada.apilar(secuencia[i].desapilar())

    

    while not pila_intercalada.esta_vacia():

        pila_resultado.apilar(pila_intercalada.desapilar())

    return pila_resultado

pila1 = Pila()
pila1.apilar(2)
pila1.apilar(1)
pila2 = Pila()
pila2.apilar(6)
pila2.apilar(5)
pila2.apilar(4)
pila2.apilar(3)
pila3 = Pila()
pila3.apilar(7)
pila = intercalar_pilas([pila1,pila2,pila3])
while not pila.esta_vacia():
    print(pila.desapilar())

