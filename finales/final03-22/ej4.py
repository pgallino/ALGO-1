import math

def buscar_cero(f, n_min, n_max):
    #
    # HACER: implementar la función
    #
    medio = (n_max + n_min) // 2

    valor = f(medio)

    if -0.000000000000000000000000001 < valor < 0.00000000000000000000000000000001:
        return medio
    
    elif valor > 0:

        return buscar_cero(f, n_min, medio)
    
    else:

        return buscar_cero(f, medio, n_max)

def pruebas():

    def f(n):
        return math.factorial(n) - 40320

    assert buscar_cero(f, 0, 20) == 8   # porque f(8) == 0

    # OPCIONAL: agregar más casos de prueba.

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
