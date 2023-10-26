"""Ejercicio 145 colas
Escribir una función que recibe una cola y un número k, y devuelve una lista de k colas, con los elementos de la cola original asignados en forma balanceada 

(las k colas deben quedar con aproximadamente la misma cantidad de elementos), y alternada. Ejemplos:

repartir(Cola([a,b,c,d,e,f,g]), 2) → [Cola([a,c,e,g]), Cola([b,d,f])]
repartir(Cola([a,b,c,d,e,f,g]), 3) → [Cola([a,d,g]), Cola([b,e]), Cola([c,f])]
repartir(Cola([a b c]), 4)         → [Cola([a]), Cola([b]), Cola([c]), Cola([])]"""

from Cola2 import Cola

def repartir_cola(cola, n):

    lista = []

    for i in range(n):
        lista.append(Cola())

    while not cola.esta_vacia():
        for i in range(n):
            if cola.esta_vacia():
                break
            lista[i].encolar(cola.desencolar())

    return lista

cola = Cola()
cola.encolar_muchos(("a","b","c","d","e","f","g"))
print(cola)

lista = repartir_cola(cola,2)


for i in range(len(lista)):
    print(lista[i])

print("fincola1")

cola2 = Cola()
cola2.encolar_muchos(("a","b","c","d","e","f","g"))
print(cola2)

lista = repartir_cola(cola2,3)


for i in range(len(lista)):
    print(lista[i])

