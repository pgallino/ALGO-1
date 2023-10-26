"""hacer una funcion recursiva que cuente los digitos de un numero"""


def contar_digitos(n):        #version piola

    if n<10:
        return 1

    k = n//10
    return 1+contar_digitos(k)

def _contar_digitos2(n, contador):                           #uso una cadena
    if len(n) == 0:
        return 0
    
    return contar_digitos(n[1:]) + 1

def contar_digitos2(n):                                      #wrapper de _contar_digitos2
    n = str(n)
    return _contar_digitos2(n, contador = 0)