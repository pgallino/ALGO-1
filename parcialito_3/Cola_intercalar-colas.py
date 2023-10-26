from Cola2 import Cola

"""Implementar una función intercalar(colas) que reciba una secuencia de colas y devuelva una cola con los elementos de todas
las colas intercalados, manteniendo el orden relativo. Las colas originales deben quedar vacías.

Ejemplo:

intercalar([Cola(1, 2), Cola(3, 4, 5, 6), Cola(7)]) -> Cola(1, 3, 7, 2, 4, 5, 6)"""

def intercalar(colas):

    cola_resultado = Cola()

    while True:
        colas_vacias = 0
        for i in range(len(colas)):
            if colas[i].esta_vacia():
                colas_vacias += 1
                continue
            cola_resultado.encolar(colas[i].desencolar())

        if colas_vacias == len(colas):
            break
    return cola_resultado

cola1 = Cola()
cola1.encolar_muchos((1,2))
cola2 = Cola()
cola2.encolar_muchos((3,4,5,6))
cola3 = Cola()
cola3.encolar(7)

print(intercalar((cola1,cola2,cola3)))
