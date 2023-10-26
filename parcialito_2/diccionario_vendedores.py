"""Se tiene un diccionario de la forma {nombre_vendedor : total_vendido}, con la suma total de lo vendido por distintos vendedores 

otro con forma {local : [nombre_vendedor_1, nombre_vendedor_2, …]}, con los vendedores que trabajan en cada local. 

Escribir una función que reciba diccionarios como los mencionados,

y devuelva un nuevo diccionario cuyas claves sean los nombres de los locales y sus valores el total vendido por los vendedores de ese local."""

def contador_total_vendido_locales(vendedores_total, locales_vendedores):

    locales_total = {}

    for clave in locales_vendedores:

        ingreso_total = 0

        for vendedor in vendedores_total:

            if vendedor in locales_vendedores[clave]:
                ingreso_total += vendedores_total[vendedor]

        locales_total[clave] = ingreso_total

    return locales_total