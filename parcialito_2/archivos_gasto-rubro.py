"""Dado un archivo con el siguiente encabezado: Día,Mes,Año,Rubro,Gasto, ordenado cronológicamente (el gasto más reciente está al final):

escribir una función que reciba el nombre de archivo y dos tuplas de la forma (mes, año).

La función debe devolver el nombre del rubro que más gastos lleva acumulados entre las fechas dadas y dicho gasto acumulado.

Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos deben quedar cerrados."""

def contar_gasto_periodo(ruta_archivo, comienzo, final):

    dic_rubros = {}

    with open(ruta_archivo) as archivo:
        mes_i, año_i = comienzo
        mes_f, año_f = final
        next(archivo)
        for linea in archivo:
            linea = linea.rstrip("\n").split(";")
            _, mes, año, rubro, gasto = linea
            if (int(año), int(mes)) >= (año_i,mes_i) and (int(año),int(mes)) < (año_f,mes_f):
                dic_rubros[rubro] = dic_rubros.get(rubro, 0) + int(gasto)

    mayor_gasto = 0
    for clave in dic_rubros:
            if mayor_gasto < dic_rubros[clave]:
                mayor_gasto = dic_rubros[clave]
                rubro_mas_gastoso = clave

    return f"el rubro que mas gasto entre {mes_i}/{año_i} y {mes_f}/{año_f} fue {rubro_mas_gastoso} con {dic_rubros[rubro_mas_gastoso]} pesos"