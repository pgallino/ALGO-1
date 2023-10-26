"""Ejercicio 154 colas

Implementar la clase ColaDistribuidora con los siguientes métodos:

ColaDistribuidora(ids, f): Crea una nueva instancia. 

ids es una lista de identificadores (cadenas), y f es una función que recibe cualquier cosa y devuelve siempre uno de los identificadores de la lista ids.

encolar(elemento): Aplica la funcion f al elemento, y según el identificador obtenido encola el elemento en una cola específica para ese identificador.

desencolar(identificador): Desencola y devuelve el elemento al frente de la cola para el identificador dado.

esta_vacia(): devuelve verdadero si todas las colas están vacías."""

from Cola2 import Cola
from random import randint

class ColaDistribuidora:

    def __init__(self, ids, f):
        self.nombres = {}
        self.identificadores = ids
        for i in ids:
            self.nombres[i] = Cola()

        self.funcion = f

    def encolar(self, elemento):
        nombre = self.funcion(self.identificadores)
        self.nombres[nombre].encolar(elemento)

    def desencolar(self, identificador):
        if not self.nombres[identificador].esta_vacia():
            return self.nombres[identificador].desencolar()

    def esta_vacia(self):
        vacias = 0
        for clave in self.nombres:
            if self.nombres[clave].esta_vacia():
                vacias += 1
            
        if vacias == len(self.nombres):
            return True
        
        return False

def funcion(ids):
    indice = randint(0, len(ids) - 1)
    return ids[indice]

ids = ["arbol","amor", "monja"]
cola = ColaDistribuidora(ids, funcion)
cola.encolar(23)
cola.encolar(12)
cola.encolar(92)
for clave in cola.nombres:
    print(f"{clave} tiene {cola.nombres[clave]}")
print(cola.esta_vacia())
cola.desencolar("monja")

for clave in cola.nombres:
    print(f"{clave} tiene {cola.nombres[clave]}")
print(cola.esta_vacia())
