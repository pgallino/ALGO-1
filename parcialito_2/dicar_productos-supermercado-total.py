"""Escribir una funcion que reciba una lista de pedidos a un supermercado, 

donde cada pedido es hecho por una persona distinta y puede tener cualquier producto, y tiene el siguiente formato:

{nombre_producto1: cant1, …, nombre_producto_n: cant_n }. 
 
La función debe escribir a un archivo que tenga el resumen de los pedidos con el siguiente formato:

nombre_producto;cant_total
donde cada producto está una única vez y la cantidad total es la cantidad de todas las personas que compraron ese producto.

Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos deben quedar cerrados."""


def cargar_productos_ingresos(lista, ruta_archivo):

    with open (ruta_archivo, "w") as archivo:
        diccionario = {}
        for pedido in lista:
            for clave in pedido:
                diccionario[clave] = diccionario.get(clave, 0) + pedido[clave]

        for clave in diccionario:
            archivo.write(f"{clave};{diccionario[clave]}\n")
