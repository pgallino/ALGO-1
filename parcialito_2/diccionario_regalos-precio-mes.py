"""Escribir una función que reciba 3 diccionarios:

 cumpleaños: sus claves son nombres de personas y los valores asociados, sus fecha de nacimiento (dd/mm/aaaa). 
 regalos: sus claves son nombres de personas y los valores asociados, el nombre del regalo que quiere cada uno para su cumpleaños. 
 precios: sus claves son nombres de regalos y sus valores asociados, el precio de cada uno.

La función debe devolver otro diccionario donde la clave es el mes y el valor asociado es la suma de los precios de los regalos de quienes cumplen años en ese mes."""

def suma_regalos_por_mes(cumpleaños, regalos, precios):
    suma_mes = {}
    for clave in cumpleaños:
        mes = cumpleaños[clave].split("/")[1]
        regalo = regalos[clave]
        precio = precios[regalo] 
        suma_mes[mes] = suma_mes.get(mes, 0) + precio
    return suma_mes
