# Escribir una funcion shift_colas que recibe una lista de colas y debe mover el contenido de cada cola con el de la siguiente. 
# Es decir, el contenido de la cola en la posicion 0 debe ir en la cola en la posición 1, el de la 1 en la 2 y el de la ultima cola, en la de la posición 0.
# Importante: tiene que rotar el contenido de las colas, NO las colas. Es decir, cada una debe mantener su posicion en la lista.
# Ejemplo:
# print(colas)
# [Cola(1,2,3), Cola(4,5,6), Cola(), Cola(7,8)]
# shift_colas(colas)
# print(colas)
# [Cola(7,8), Cola(1,2,3), Cola(4,5,6), Cola()]

from tda import Pila, Cola

# Completar la siguiente funcion
def shift_colas(colas):
    aux = Cola()
    for i in range(len(colas) -1, 0, -1):
        while not colas[i].esta_vacia():
            aux.encolar(colas[i].desencolar())
        while not colas[i-1].esta_vacia():
            colas[i].encolar(colas[i-1].desencolar())
        while not aux.esta_vacia():
            colas[i-1].encolar(aux.desencolar())

# Pruebas
original = [Cola() for i in range(4)]
original[0].encolar_desde([1,2,3])
original[1].encolar_desde([4,5,6])
original[3].encolar_desde([7,8])
res = [Cola() for i in range(4)]
res[1].encolar_desde([1,2,3])
res[2].encolar_desde([4,5,6])
res[0].encolar_desde([7,8])
shift_colas(original)
for i in range(len(original)):
    assert original[i] == res[i]

            
