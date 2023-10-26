"""Ejercicio 156 recursion

Realizar una función recursiva en Python que reciba un número entero y devuelva el producto de sus dígitos. 

Ejemplo: producto_digital(356) → 90, pues 3 * 5 * 6 = 90."""

def producto_digital(numero):

    if type(numero) != str:
        numero = str(numero)
    
    if len(numero) == 1:
        return int(numero[0])
    
    return producto_digital(numero[1:]) * int(numero[0])


print(producto_digital(356))



