def resumir_pedidos(pedidos, nombre_archivo_dest):
    '''
    Escribir una función que reciba una lista de pedidos de un supermercado,
    donde cada pedido es un diccionario con el siguiente formato:

    { nombre_producto1: cant1, …, nombre_producto_n: cant_n }
    Y escriba un archivo que tenga el resumen de los pedidos con el siguiente formato (sin cabecera):

    nombre_producto;cant_total
    Siendo cant_total el stock total de ese producto que fue solicitado entre todos los pedidos.
    '''

    with open(nombre_archivo_dest, "w") as archivo:
        diccionario_enorme = {}
        for pedido in pedidos:
            for clave in pedido:
                diccionario_enorme[clave] = diccionario_enorme.get(clave, 0) + pedido[clave]

        for clave in diccionario_enorme:
            archivo.write(f"{clave};{diccionario_enorme[clave]}\n")