# 3. Escribir una función que, dada una cola y un elemento E, devuelva cuántos elementos
# faltan para que salga E de la cola. Si E no está en la cola,
# debe levantarse una excepción. Al finalizar la ejecución, La cola debe quedar en 
# su estado original para cualquiera de los casos posibles.

# Ejemplo (donde el primer elemento a salir es el 4)

# entra >| 11 10  9  7  6  4 |> sale
# El elemento 7 está a dos elementos de salir


from tda import Pila, Cola

# Completar la siguiente funcion
def cantidad_restante(cola, elemento):
    
    contador = 0
    primera_vez = 0
    cola_aux = Cola()

    while not cola.esta_vacia():

        dato = cola.ver_frente()
        if dato == elemento:
            primera_vez += 1
            if primera_vez == 1:
                falta = contador
        cola_aux.encolar(cola.desencolar())
        contador += 1
    
    while not cola_aux.esta_vacia():
        cola.encolar(cola_aux.desencolar())
    
    if primera_vez == 0:
        raise exception
    
    return falta
            



c = Cola([4, 6, 7, 9, 10, 11])
assert cantidad_restante(c, 7) == 2

hay_excepcion = True
try:
    cantidad_restante(c, 5)
    hay_excepcion = False
except:
    pass
assert hay_excepcion, "una excepcion no fue lanzada"
