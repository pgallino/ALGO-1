"""funcion recursiva que devuelva el elemento mayor de un arreglo"""

def _obtener_mayor_elemento(arr, valor, valor_maximo):

    if arr == []:
        return valor_maximo
    
    valor = arr[0]
    if valor > valor_maximo:
        valor_maximo = valor
    
    return _obtener_mayor_elemento(arr[1:], valor, valor_maximo)

def obtener_mayor_elemento(arr):
    valor = 0
    valor_maximo = 0
    return _obtener_mayor_elemento(arr, valor, valor_maximo)