from random import randint
def generar(n):
    # HACER: implementar la función
    lista = []
    for i in range(n):
        lista.append(randint(0,100))
    
    return lista

def ordenar(a):
    # HACER: implementar la función
    for j in range(len(a)):
        for i in range(1,len(a)):
            if a[i-1] > a[i]:
                a[i-1] , a[i] = a[i], a[i-1]

#esta funcion es t(n**2) aproximadamente ya que hay un ciclo adentro del otro.
#el estacio es cte, se usa el espacio de la lista y alguna que otra variable.

def pruebas():
    L = [5, 2, 3, 1, 4]
    ordenar(L)
    assert L == [1, 2, 3, 4, 5]

    from timeit import timeit
    for n in [1, 10, 100, 500, 1000, 5000, 10000]:
        print(f"Probando con n = {n}")

        # generamos una lista a ordenar
        L = generar(n)

        # ordenamos y medimos cuánto tiempo tarda
        s = timeit(lambda: ordenar(L), number=1)

        # verificamos que está ordenada
        assert all(L[i] >= L[i-1] for i in range(1, len(L)))

        print(f"  OK -- {s:.2f} segundos")

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
