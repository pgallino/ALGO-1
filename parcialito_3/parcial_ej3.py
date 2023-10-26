# Dado un arreglo de enteros y un número `k`, escribir una función `obtener_suma_maxima`
# que devuelve la mayor suma posible entre `k` elementos contiguos del arreglo.
# Ejemplos:
# obtener_suma_maxima([3, 1, 9, 2, 3, 6], 3)  =>  Devuelve 14, por la suma de [9, 2, 3]
# obtener_suma_maxima([3, 1, 9, 2, 3, 6], 4)  =>  Devuelve 20, por la suma de [9, 2, 3, 6]
# obtener_suma_maxima([3, 1, 9, 2, 3, 6], 15)  =>  Devuelve 24, por la suma de todo el arreglo

from tda import Cola, Pila

#Completar la siguiente funcion
def obtener_suma_maxima(arr, k):
    cola= Cola()
    semi_cola = Cola()
    mayor_suma = 0
    contador = 0

    for indice in arr:
        cola.encolar(indice)

    for i in range(k):
        if cola.esta_vacia():
            break
        contador += 1
        semi_cola.encolar(cola.desencolar())

    if contador < k:
        while not semi_cola.esta_vacia():
            mayor_suma += semi_cola.desencolar()
        
        return mayor_suma

    while not cola.esta_vacia():
        
        suma = 0

        for i in range(k):

            dato = semi_cola.desencolar()
            semi_cola.encolar(dato)
            suma += dato

        semi_cola.desencolar()
        semi_cola.encolar(cola.desencolar())

        if suma > mayor_suma:
            mayor_suma = suma

    suma = 0

    while not semi_cola.esta_vacia():
        suma += semi_cola.desencolar()

    if suma > mayor_suma:
        mayor_suma = suma
    
    return mayor_suma




res1 = obtener_suma_maxima([3, 1, 9, 2, 3, 6], 3)
res2 = obtener_suma_maxima([3, 1, 9, 2, 3, 6], 4)
res3 = obtener_suma_maxima([3, 1, 9, 2, 3, 6], 15)
assert res1 == 14 and res2 == 20 and res3 == 24